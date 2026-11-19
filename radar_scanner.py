"""
pine-radar: Spatial Radar Scanner & Landmark Detection Engine
Autonomous coordinate scanning with 60-meter physical clearance proximity checks.
"""

import math
from typing import List, Dict, Any, Tuple, Optional

class RadarScanner:
    """Performs spatial radial sweeps and verifies object proximity clearances."""

    def __init__(self, default_origin: Tuple[float, float] = (45.0, 45.0)):
        self.default_origin = default_origin

    def calculate_distance(self, p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        """Euclidean distance in meters between two coordinates."""
        return round(math.hypot(p2[0] - p1[0], p2[1] - p1[1]), 2)

    def calculate_bearing(self, origin: Tuple[float, float], target: Tuple[float, float]) -> float:
        """Calculate compass bearing in degrees (0-360) from origin to target."""
        dx = target[0] - origin[0]
        dy = target[1] - origin[1]
        bearing = math.degrees(math.atan2(dx, dy))
        return round((bearing + 360.0) % 360.0, 1)

    def scan_sector(
        self,
        origin: Optional[Tuple[float, float]] = None,
        radius: float = 150.0,
        max_range: Optional[float] = None,
        min_clearance: float = 60.0,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Execute a radial sweep across the grid coordinates.
        Supports both 'radius' and 'max_range' keyword arguments seamlessly.
        """
        scan_radius = max_range if max_range is not None else radius
        center = origin if origin is not None else self.default_origin

        # Known coordinate landmarks for verification and navigation
        reference_landmarks = [
            {"name": "TreeberryPine", "coords": (45.0, 45.0), "type": "tree"},
            {"name": "Solar Pinecone Relay Tower", "coords": (120.0, 150.0), "type": "sensor"},
            {"name": "Train Station", "coords": (320.0, 440.0), "type": "landmark"},
            {"name": "Vercel Photonic Uplink Gateway", "coords": (-120.0, -60.0), "type": "contraption"},
            {"name": "Quartz Packet Repeater", "coords": (-180.0, -120.0), "type": "contraption"},
            {"name": "Beryllium-Quartz Harmonic Resonator", "coords": (-250.0, -100.0), "type": "contraption"},
            {"name": "Bistable Morphological Inclinometer", "coords": (-330.0, -210.0), "type": "contraption"},
        ]

        detected: List[Dict[str, Any]] = []
        clearance_warnings: List[Dict[str, Any]] = []

        for item in reference_landmarks:
            dist = self.calculate_distance(center, item["coords"])
            bearing = self.calculate_bearing(center, item["coords"])

            if dist <= scan_radius:
                is_clear = (dist >= min_clearance) or (dist == 0.0)
                entry = {
                    "name": item["name"],
                    "coords": item["coords"],
                    "type": item["type"],
                    "distance_m": dist,
                    "bearing_deg": bearing,
                    "clearance_ok": is_clear
                }
                detected.append(entry)
                if not is_clear and dist > 0.0:
                    clearance_warnings.append(entry)

        detected.sort(key=lambda x: x["distance_m"])

        return {
            "origin": center,
            "scan_radius_m": scan_radius,
            "min_clearance_m": min_clearance,
            "targets_detected": len(detected),
            "clearance_violations": len(clearance_warnings),
            "targets": detected,
            "status": "CLEAR" if not clearance_warnings else "PROXIMITY_WARNING"
        }