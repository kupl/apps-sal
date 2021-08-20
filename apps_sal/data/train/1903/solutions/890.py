from collections import defaultdict
import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        (total, heap, visited) = (0, [(0, 0)], set())
        distances = defaultdict(list)
        for i in range(len(points) - 1):
            for j in range(1, len(points)):
                distances[i].append((self.distance(points[i], points[j]), j))
                distances[j].append((self.distance(points[i], points[j]), i))
        while heap and len(visited) < len(points):
            (distance, point) = heapq.heappop(heap)
            if point not in visited:
                visited.add(point)
                total += distance
                for (neighbor_distance, neighbor) in distances[point]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (neighbor_distance, neighbor))
        return total

    def distance(self, pair1, pair2):
        return abs(pair1[0] - pair2[0]) + abs(pair1[1] - pair2[1])
