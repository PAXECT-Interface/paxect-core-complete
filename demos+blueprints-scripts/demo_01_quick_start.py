#!/usr/bin/env python3
"""
PAXECT Demo 01 – Quick Start
-----------------------------
5-minute verification test for new users.
Shows: Installation check + ready-to-use confirmation
"""
import json

MODULES = [
    "paxect_core_plugin",
    "paxect_aead_hybrid_plugin",
    "paxect_polyglot_plugin",
    "paxect_selftune_plugin",
    "paxect_link_plugin",
]

def main():
    print("=" * 60)
    print("  PAXECT Quick Start – Installation Verification")
    print("=" * 60)
    print()
    
    # Check modules
    all_ok = True
    for name in MODULES:
        try:
            __import__(name)
            print(f"✓ {name:30} OK")
        except Exception as e:
            print(f"✗ {name:30} FAILED: {e}")
            all_ok = False
    
    print()
    print("=" * 60)
    
    if all_ok:
        print("✓ SUCCESS: PAXECT is ready to use!")
        print()
        print("Next steps:")
        print("  → Process messages:    python3 demos/demo_02_integration_loop.py")
        print("  → Test encryption:     python3 demos/demo_08_secure_multichannel_aead_hybrid.py")
        print("  → Full enterprise:     python3 demos/demo_09_enterprise_all_in_one.py")
        print()
        print("Documentation: https://github.com/PAXECT-Interface/paxect-core-complete")
    else:
        print("✗ INSTALLATION INCOMPLETE")
        print()
        print("Fix: Run installation again:")
        print("  pip install -e .")
        return 1
    
    print("=" * 60)
    return 0

if __name__ == "__main__":
    exit(main())
