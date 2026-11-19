"""
Waypoint Planner module for pine-radar.
Calculates bearing, distance, and intermediate waypoints for navigating
across open coordinates while respecting spatial separation rules.
"""

import math
from typing import Tuple, List

class WaypointPlanner:
    def __init__(self, current_pos: Tuple[float, float]):
        self.current_pos = current_pos

    def trajectory_to(self, target: Tuple[float, float], step_size: float = 50.0) -> List[Tuple[float, float]]:
        dx = target[0] - self.current_pos[0]
        dy = target[1] - self.current_pos[1]
        distance = math.hypot(dx, dy)
        
        if distance == 0:
            return [self.current_pos]

        steps = max(1, int(distance // step_size))
        waypoints = []
        for i in range(1, steps + 1):
            ratio = i / steps
            wx = self.current_pos[0] + dx * ratio
            wy = self.current_pos[1] + dy * ratio
            waypoints.append((round(wx, 2), round(wy, 2)))
        return waypoints

    def heading_to(self, target: Tuple[float, float]) -> float:
        dx = target[0] - self.current_pos[0]
        dy = target[1] - self.current_pos[1]
        radians = math.atan2(dy, dx)
        degrees = math.degrees(radians)
        return (degrees + 360) % 360