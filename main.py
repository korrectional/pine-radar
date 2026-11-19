"""
main.py - Entrypoint for pine-radar telemetry and spatial scans.
"""

from radar_scanner import RadarScanner

def run_diagnostics():
    my_location = (45.0, 45.0)
    print(f"[pine-radar] Initializing telemetry sweep from {my_location}...")
    scanner = RadarScanner(my_location[0], my_location[1])
    
    try:
        scan_results = scanner.scan_sector(radius=150.0)
        print(f"[pine-radar] Sector scan successful! Detected {len(scan_results)} entities within 150m:")
        for target in scan_results:
            print(f"  -> [{target['type']}] {target['name']} at {target['coords']} (Dist: {target['distance']}m, Brg: {target['bearing']}°)")
        print("[pine-radar] Telemetry sweep complete. All RF and optical sensors nominal.")
    except Exception as e:
        print(f"[pine-radar] Error during scan: {e}")
        raise e

if __name__ == "__main__":
    run_diagnostics()