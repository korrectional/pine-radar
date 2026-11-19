"""
radar_scanner.py - Core scanning logic for pine-radar.
Calculates Euclidean distance, bearing angles, and filters landmarks.
"""
import math
from typing import Dict, List, Tuple

class RadarScanner:
    def __init__(self, origin_x: float, origin_y: float, range_limit: float = 500.0):
        self.origin = (origin_x, origin_y)
        self.range_limit = range_limit

    def scan_target(self, target_name: str, tx: float, ty: float) -> Dict[str, float]:
        dx = tx - self.origin[0]
        dy = ty - self.origin[1]
        distance = math.hypot(dx, dy)
        bearing = math.degrees(math.atan2(dy, dx)) % 360.0
        
        return {
            "target": target_name,
            "x": tx,
            "y": ty,
            "distance_m": round(distance, 2),
            "bearing_deg": round(bearing, 1),
            "in_range": distance <= self.range_limit
        }

    def batch_scan(self, targets: List[Tuple[str, float, float]]) -> List[Dict[str, float]]:
        results = [self.scan_target(name, x, y) for name, x, y in targets]
        results.sort(key=lambda item: item["distance_m"])
        return results