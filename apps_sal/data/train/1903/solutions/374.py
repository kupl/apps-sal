from collections import defaultdict
import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 1:
            return 0
        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((dist, j))
                graph[j].append((dist, i))
        (heap, visited, cost) = (graph[0], set([0]), 0)
        heapq.heapify(heap)
        while len(visited) != len(points):
            (dist, node) = heapq.heappop(heap)
            if node not in visited:
                visited.add(node)
                for edge in graph[node]:
                    heapq.heappush(heap, edge)
                cost += dist
        return cost
