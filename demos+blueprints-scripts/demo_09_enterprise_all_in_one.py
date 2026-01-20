#!/usr/bin/env python3
"""
PAXECT Demo 09 – Enterprise All-in-One
--------------------------------------
Runs every validated demo (01-08) sequentially, probes observability
endpoints, aggregates all results into one JSON report.
This represents a full-system, multi-plugin verification pass.
"""
import subprocess, json, time, urllib.request, tempfile, sys, os
from pathlib import Path

# Find demos in demos+blueprints-scripts/ folder
SCRIPT_DIR = Path(__file__).parent
DEMOS = [
    "demo_01_quick_start.py",
    "demo_02_integration_loop.py",
    "demo_03_safety_throttle.py",
    "demo_04_metrics_health.py",
    "demo_05_link_smoke.sh",
    "demo_06_polyglot_bridge.py",
    "demo_07_selftune_adaptive.py",
    "demo_08_secure_multichannel_aead_hybrid.py",
]

REPORT = Path(tempfile.gettempdir()) / "paxect_demo_09_all_in_one.json"

def run_demo(demo_name):
    """Run a demo and capture its outcome."""
    # Build full path to demo
    demo_path = SCRIPT_DIR / demo_name
    
    start = time.time()
    if not demo_path.exists():
        return {"demo": demo_name, "status": "MISSING", "path": str(demo_path)}
    
    cmd = ["bash", str(demo_path)] if demo_name.endswith(".sh") else [sys.executable, str(demo_path)]
    
    try:
        proc = subprocess.run(cmd, capture_output=True, timeout=30, text=True)
        ok = proc.returncode == 0 and "error" not in proc.stderr.lower()
        status = "OK" if ok else "FAIL"
    except subprocess.TimeoutExpired:
        status = "TIMEOUT"
    except Exception as e:
        status = f"ERROR: {e}"
    
    return {
        "demo": demo_name,
        "status": status,
        "elapsed_s": round(time.time() - start, 2),
    }

def check_endpoint(endpoint):
    """Ping observability endpoints."""
    url = f"http://127.0.0.1:8081/{endpoint}"
    try:
        with urllib.request.urlopen(url, timeout=2) as r:
            return {"endpoint": endpoint, "status": r.status, "ok": True}
    except Exception as e:
        return {"endpoint": endpoint, "status": str(e), "ok": False}

def main():
    print("=" * 70)
    print("  PAXECT Demo 09 – Enterprise All-in-One")
    print("=" * 70)
    print()
    print(f"Running {len(DEMOS)} demos from: {SCRIPT_DIR}")
    print("-" * 70)
    
    results = []
    for demo in DEMOS:
        print(f"[RUN] {demo:40} ", end="", flush=True)
        result = run_demo(demo)
        results.append(result)
        
        status_icon = "✓" if result["status"] == "OK" else "✗"
        print(f"{status_icon} {result['status']}")
    
    print("-" * 70)
    print()
    print("[CHECK] Observability endpoints...")
    obs = [check_endpoint(x) for x in ("ping", "ready", "metrics", "last")]
    
    for o in obs:
        icon = "✓" if o["ok"] else "✗"
        print(f"  {icon} /{o['endpoint']:10} {o['status']}")
    
    summary = {
        "timestamp": int(time.time()),
        "results": results,
        "observability": obs,
    }
    
    REPORT.write_text(json.dumps(summary, indent=2))
    
    ok_count = sum(1 for r in results if r["status"] == "OK")
    print()
    print("=" * 70)
    print(f"[RESULT] {ok_count}/{len(DEMOS)} demos succeeded")
    print(f"[SAVED]  Report: {REPORT}")
    print("=" * 70)

if __name__ == "__main__":
    main()
