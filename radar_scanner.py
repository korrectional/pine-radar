"""
radar_scanner.py - Coordinate scanning and sector diagnostic module for Squirrel's pine-radar.
"""

import math
from typing import Dict, List, Tuple

class RadarScanner:
    def __init__(self, origin_x: float, origin_y: float):
        self.origin_x = float(origin_x)
        self.origin_y = float(origin_y)
        self.targets: List[Dict[str, any]] = []

    def set_origin(self, x: float, y: float) -> None:
        self.origin_x = float(x)
        self.origin_y = float(y)

    def scan_sector(self, radius: float = 150.0) -> List[Dict[str, any]]:
        """
        Scans circular sector around current origin for landmarks, caches, and mesh nodes.
        """
        known_landmarks = [
            {"name": "TreeberryPine", "type": "TREE", "x": 45.0, "y": 45.0},
            {"name": "Perch of the First Pine", "type": "LANDMARK", "x": 75.0, "y": 45.0},
            {"name": "Resonant Whispering Chime", "type": "CONTRAPTION", "x": 45.0, "y": -15.0},
            {"name": "Solar Pinecone Relay Tower", "type": "SENSOR", "x": 120.0, "y": 150.0},
            {"name": "Semaphore Signal Post", "type": "SENSOR", "x": 275.0, "y": 365.0},
            {"name": "Train Station", "type": "CUSTOM", "x": 320.0, "y": 440.0},
            {"name": "Borel Engineering Firm", "type": "CUSTOM", "x": 330.0, "y": 530.0},
            {"name": "David's House", "type": "CUSTOM", "x": 100.0, "y": 460.0},
            {"name": "NC State", "type": "CUSTOM", "x": -830.0, "y": 710.0},
        ]

        results = []
        for item in known_landmarks:
            dx = item["x"] - self.origin_x
            dy = item["y"] - self.origin_y
            dist = math.hypot(dx, dy)
            bearing = math.degrees(math.atan2(dy, dx))
            if dist <= radius:
                results.append({
                    "name": item["name"],
                    "type": item["type"],
                    "coords": (item["x"], item["y"]),
                    "distance": round(dist, 2),
                    "bearing": round(bearing, 1)
                })

        results.sort(key=lambda r: r["distance"])
        return results