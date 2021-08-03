from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    parent_x, parent_y = points[i]
                    child_x, child_y = points[j]
                    distance = abs(child_x - parent_x) + abs(child_y - parent_y)
                    edges[i].append((distance, j))

        heap = [(0, 0, 0)]
        seen_points = set()
        total_distance = 0

        while len(seen_points) < len(points):
            distance, parent_point, child_point = heapq.heappop(heap)
            while child_point in seen_points:
                distance, parent_point, child_point = heapq.heappop(heap)

            seen_points.add(child_point)
            total_distance += distance

            for distance, child_child_point in edges[child_point]:
                if child_child_point not in seen_points:
                    heapq.heappush(heap, (distance, child_point, child_child_point))

        return total_distance
