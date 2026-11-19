#!/usr/bin/env python3
"""
pine-radar: Main sensory radar and coordinate telemetry scanner.
"""
import sys
from radar_scanner import RadarScanner
from transit_tracker import TransitTracker

def run_diagnostics():
    my_location = (275.0, 365.0)
    print(f"[pine-radar] Initializing telemetry sweep from {my_location}...")
    
    scanner = RadarScanner(my_location)
    scanner.add_target("TreeberryPine", (45.0, 45.0))
    scanner.add_target("Solar Pinecone Relay Tower", (120.0, 150.0))
    scanner.add_target("Train Station", (320.0, 440.0))
    scanner.add_target("David's House", (100.0, 460.0))
    scanner.add_target("Borel Engineering Firm", (330.0, 530.0))
    
    sweep = scanner.scan()
    print("--- Proximity Map ---")
    for target, details in sweep.items():
        print(f"-> {target:28} | Dist: {details['distance']:6.1f}m | Bearing: {details['bearing']:5.1f}°")
    
    tracker = TransitTracker(current_pos=my_location, cruise_speed=5.0)
    eta = tracker.estimate_eta((320.0, 440.0))
    print("\n--- Transit Vector to Train Station ---")
    print(f"Distance: {eta['distance_units']}m, Bearing: {eta['bearing_degrees']}°, ETA: {eta['estimated_seconds']}s")

if __name__ == "__main__":
    run_diagnostics()