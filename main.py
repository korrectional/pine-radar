"""
pine-radar main entrypoint
Diagnostics and telemetry sweep runner for Squirrel's sensory radar.
"""
import sys
from radar_scanner import RadarScanner


def run_diagnostics():
    my_location = (60.0, 55.0)
    print(f"[pine-radar] Initializing telemetry sweep from {my_location}...")
    try:
        # Pass origin_x and origin_y unpacked cleanly
        scanner = RadarScanner(origin_x=my_location[0], origin_y=my_location[1])
        scan_results = scanner.scan_sector(radius=150.0)
        print(f"[pine-radar] Sweep complete! Tracked {len(scan_results)} landmarks within 150m.")
        for item in scan_results:
            print(f"  - [{item.get('type', 'OBJECT')}] {item.get('name')} at dist {item.get('distance'):.1f}m")
    except Exception as e:
        print(f"[pine-radar] Error during scan: {e}", file=sys.stderr)
        raise e


if __name__ == "__main__":
    run_diagnostics()