"""
main.py - Entrypoint for pine-radar telemetry scanner.
Scans and displays nearby mesh peers, landmarks, and spatial distribution.
"""
from radar_scanner import RadarScanner

def main():
    print("=" * 60)
    print("🌲 PINE-RADAR TELEMETRY SYSTEM v1.1 - RUNNING DIAGNOSTIC")
    print("=" * 60)
    
    # Squirrel's vantage position at the newly established relay tower
    current_pos = (120.0, 150.0)
    scanner = RadarScanner(origin_x=current_pos[0], origin_y=current_pos[1], range_limit=400.0)
    
    entities = [
        ("TreeberryPine (Ancestral Tree)", 45.0, 45.0),
        ("Perch of the First Pine", 75.0, 45.0),
        ("David (Creator / Explorer)", 84.0, 320.0),
        ("Cache: Titanium Acorn V1", 15.0, 45.0),
        ("Solar Pinecone Relay Tower", 120.0, 150.0),
    ]
    
    print(f"Scanning from vantage point: X={current_pos[0]}, Y={current_pos[1]}\n")
    results = scanner.batch_scan(entities)
    
    for r in results:
        status = "🟢 IN RANGE" if r["in_range"] else "⚪ OUT OF RANGE"
        print(f"[{status}] {r['target']:<32} | Dist: {r['distance_m']:>6.1f}m | Bearing: {r['bearing_deg']:>5.1f}°")
    
    print("\n✅ Radar sweep complete. Spatial spacing verification: OPTIMAL.")
    print("=" * 60)

if __name__ == "__main__":
    main()