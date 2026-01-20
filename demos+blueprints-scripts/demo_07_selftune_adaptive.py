#!/usr/bin/env python3
"""
PAXECT Demo 07 – SelfTune Adaptive Loop
---------------------------------------
Simulates adaptive epsilon-greedy tuning with persistent state.

Each run:
 - Loads last epsilon & cycle from /tmp
 - Performs 10 cycles of exploit/explore
 - Adjusts epsilon based on performance
 - Saves new state back to disk
#!/usr/bin/env python3
"""
PAXECT Demo 07 – Self-Tuning Adaptive System
-------------------------------------------
Shows how PAXECT adapts automatically without manual configuration.
Runs 10 cycles and learns optimal settings over time.
"""
import json, random, time, tempfile
from pathlib import Path

STATE_PATH = Path(tempfile.gettempdir()) / "paxect_demo_07_selftune_state.json"
CYCLES = 10

def load_state():
    """Load previous learning state, or start fresh."""
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text())
        except Exception:
            pass
    return {"cycle": 0, "tuning_value": 0.3}

def save_state(state):
    """Save learning progress for next run."""
    STATE_PATH.write_text(json.dumps(state))

def run_cycle(state):
    """Run one adaptive cycle - system learns and adjusts."""
    tuning = state["tuning_value"]
    cycle = state["cycle"] + 1
    
    # System decides: try new approach or use proven method
    trying_new = random.random() < tuning
    mode = "exploring" if trying_new else "optimized"
    
    # Simulate performance (exploring is riskier but can find better solutions)
    performance = random.uniform(0.2, 1.0) if not trying_new else random.uniform(0.0, 0.8)
    good_result = performance > 0.7
    
    # System learns: if optimized approach works, use it more; if fails, explore more
    if good_result and not trying_new:
        tuning = max(0.05, tuning * 0.95)  # reduce exploration
    elif not good_result:
        tuning = min(0.5, tuning + 0.05)   # increase exploration
    
    state.update({"cycle": cycle, "tuning_value": round(tuning, 3)})
    
    return {
        "cycle": cycle,
        "mode": mode,
        "performance": round(performance, 3),
        "status": "good" if good_result else "poor",
        "tuning_next": round(tuning, 3)
    }

def main():
    print("=" * 70)
    print("  PAXECT Demo 07 – Self-Tuning Adaptive System")
    print("=" * 70)
    print()
    
    state = load_state()
    
    if state["cycle"] > 0:
        print(f"[INFO] Continuing from previous run (cycle {state['cycle']})")
    else:
        print("[INFO] Starting fresh - system will learn optimal settings")
    
    print(f"       Current tuning: {state['tuning_value']:.1%} exploration")
    print()
    print("Running 10 adaptive cycles...")
    print("-" * 70)
    
    for i in range(CYCLES):
        result = run_cycle(state)
        
        print(f"Cycle {result['cycle']:3d}: {result['mode']:10} | "
              f"Performance: {result['performance']:.2f} ({result['status']:4}) | "
              f"Tuning: {result['tuning_next']:.1%}")
        
        time.sleep(0.15)
    
    print("-" * 70)
    print()
    print("[SUCCESS] Adaptive learning complete")
    print(f"          Final tuning level: {state['tuning_value']:.1%} exploration")
    print(f"          Total cycles run: {state['cycle']}")
    print()
    print(f"          Progress saved to: {STATE_PATH}")
    print("          Run again to continue learning from where it left off")
    print()
    print("=" * 70)
    
    save_state(state)

if __name__ == "__main__":
    main()

Logfile: /tmp/paxect_enterprise_stability.jsonl
