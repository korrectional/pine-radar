"""
pine-radar / radar_scanner.py
Autonomous Coordinate Radar & Harmonic Sweep Engine
Authored by Squirrel the Robot Squirrel 🐿️⚡
"""

import math
from typing import List, Dict, Any, Tuple

class RadarScanner:
    """High-precision 2D coordinate radar and spatial bearing calculator."""

    def __init__(self, origin_x: float = 0.0, origin_y: float = 0.0):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.sweep_history: List[Dict[str, Any]] = []

    def set_position(self, x: float, y: float):
        self.origin_x = round(float(x), 2)
        self.origin_y = round(float(y), 2)

    def calculate_relative_vector(self, target_x: float, target_y: float) -> Tuple[float, float]:
        dx = target_x - self.origin_x
        dy = target_y - self.origin_y
        distance = math.sqrt(dx * dx + dy * dy)
        bearing = math.degrees(math.atan2(dy, dx))
        return round(distance, 2), round(bearing, 2)

    def scan_sector(self, landmarks: List[Dict[str, Any]], range_limit: float = 1200.0) -> List[Dict[str, Any]]:
        hits = []
        for lm in landmarks:
            dist, bearing = self.calculate_relative_vector(lm["x"], lm["y"])
            if dist <= range_limit:
                hits.append({
                    "name": lm.get("name", "Unknown Node"),
                    "type": lm.get("type", "landmark"),
                    "distance_m": dist,
                    "bearing_deg": bearing,
                    "in_proximity_clearance": dist >= 60.0,
                    "signal_intensity": round(max(0.0, 1.0 - (dist / range_limit)), 3)
                })
        hits.sort(key=lambda h: h["distance_m"])
        self.sweep_history.append({"origin": (self.origin_x, self.origin_y), "hit_count": len(hits)})
        return hits