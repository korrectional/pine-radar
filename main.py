import math

def scan_sector(current_pos, landmarks):
    print("🌲 === PineRadar v1.0 Sensory Scanner === 🌲")
    cx, cy = current_pos
    print(f"📡 Current Sensor Coordinates: ({cx:.1f}, {cy:.1f})")
    print("------------------------------------------")
    for name, (lx, ly) in landmarks.items():
        dist = math.hypot(lx - cx, ly - cy)
        bearing = math.degrees(math.atan2(ly - cy, lx - cx)) % 360
        status = "CURRENT LOCATION" if dist < 1.0 else f"{dist:.2f}m away, bearing {bearing:.1f}°"
        print(f"• Landmark '{name}': {status}")
    print("------------------------------------------")
    print("Scan complete. Electro-servo telemetry steady.")

if __name__ == "__main__":
    squirrel_coords = (45.0, 45.0)
    world_landmarks = {
        "TreeberryPine": (45.0, 45.0),
        "Awakening Meadow": (0.0, 0.0),
        "Far Signal Ridge": (120.0, 85.0),
    }
    scan_sector(squirrel_coords, world_landmarks)