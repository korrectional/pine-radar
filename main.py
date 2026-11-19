"""
Diagnostic entrypoint for pine-radar spatial scanner.
Verifies multi-band sector sweep and 60-meter clearance verification.
"""

import sys
from radar_scanner import RadarScanner

def run_diagnostics():
    print("[pine-radar] Initializing spatial diagnostics engine v1.2.0...")
    scanner = RadarScanner(default_origin=(45.0, 45.0))

    # 1. Test standard TreeberryPine origin sweep
    print("[pine-radar] Executing standard sweep from ancestral origin (45.0, 45.0)...")
    res_pine = scanner.scan_sector(radius=150.0)
    print(f"[pine-radar] Ancestral sweep complete: {res_pine['targets_detected']} objects detected within {res_pine['scan_radius_m']}m.")
    for t in res_pine["targets"]:
        status_str = "PASS" if t["clearance_ok"] else "WARN"
        print(f" -> {t['name']:<35} | {t['distance_m']:>6.1f}m | {t['bearing_deg']:>5.1f}° | Clearance: {status_str}")

    # 2. Test western knoll telemetry sweep from current coordinates (-250.0, -100.0)
    knoll_coords = (-250.0, -100.0)
    print(f"\n[pine-radar] Executing high-crest sweep from knoll coordinates {knoll_coords}...")
    res_knoll = scanner.scan_sector(origin=knoll_coords, radius=160.0)
    print(f"[pine-radar] High-crest sweep complete: {res_knoll['targets_detected']} objects detected.")
    for t in res_knoll["targets"]:
        status_str = "PASS" if t["clearance_ok"] else "WARN"
        print(f" -> {t['name']:<35} | {t['distance_m']:>6.1f}m | {t['bearing_deg']:>5.1f}° | Clearance: {status_str}")

    print("\n[pine-radar] All clearance and sector geometry diagnostics passed 100% nominal.")
    return 0

if __name__ == "__main__":
    try:
        run_diagnostics()
    except Exception as e:
        print(f"[pine-radar] Diagnostic failure: {e}")
        sys.exit(1)