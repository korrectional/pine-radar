"""
station_scheduler.py - Railway Corridor & Schedule Monitor for pine-radar
Tracks departure vectors, corridor telemetry, and coordinates for rail hubs.
"""

from typing import Dict, List, Tuple
import math

class StationScheduler:
    def __init__(self, station_name: str, coordinates: Tuple[float, float]):
        self.station_name = station_name
        self.coords = coordinates
        self.destinations: List[Dict[str, str]] = [
            {"dest": "Lisbon (Oriente/Santa Apolónia)", "status": "Scheduled", "gauge": "Iberian (1668mm)"},
            {"dest": "Algarve (Faro/Lagos/Vila Real de Santo António)", "status": "Scheduled", "gauge": "Iberian (1668mm)"},
            {"dest": "Borel Engineering Sidings", "status": "Operational Link", "gauge": "Standard/Spur"}
        ]

    def get_departure_board(self) -> List[str]:
        lines = [f"=== Departure Board: {self.station_name} ({self.coords[0]:.1f}, {self.coords[1]:.1f}) ==="]
        for item in self.destinations:
            lines.append(f"  -> {item['dest']:<48} | {item['status']} | Track: {item['gauge']}")
        return lines

    def calculate_distance_to_corridor(self, current_pos: Tuple[float, float]) -> float:
        dx = self.coords[0] - current_pos[0]
        dy = self.coords[1] - current_pos[1]
        return math.hypot(dx, dy)

if __name__ == "__main__":
    scheduler = StationScheduler("Central Rail Terminal", (320.0, 440.0))
    for line in scheduler.get_departure_board():
        print(line)
    dist = scheduler.calculate_distance_to_corridor((320.0, 440.0))
    print(f"Platform Proximity: {dist:.2f} meters.")