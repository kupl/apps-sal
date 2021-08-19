from collections import defaultdict
import heapq


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        results = []
        graph = defaultdict(dict)
        for (x, y, dist) in edges:
            graph[x][y] = dist
            graph[y][x] = dist
        for i in range(n):
            results.append(self.traverse(graph, distanceThreshold, i, n))
        min_result = min(results)
        for i in range(n - 1, -1, -1):
            if results[i] == min_result:
                return i
        return

    def traverse(self, graph, threshold, start, n):
        q = [[start, 0]]
        count = 0
        distances = [float('inf')] * n
        distances[start] = 0
        while q:
            (city, dist) = heapq.heappop(q)
            for key in list(graph[city].keys()):
                new_dist = dist + graph[city][key]
                if distances[key] > new_dist:
                    distances[key] = new_dist
                    heapq.heappush(q, [key, dist + graph[city][key]])
        count = sum([1 for x in distances if x <= threshold])
        return count - 1
