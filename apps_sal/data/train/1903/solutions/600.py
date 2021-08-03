from heapq import *
from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points):
        N = len(points)
        def dist(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        edges = defaultdict(list)
        for i1, p1 in enumerate(points):
            for i2, p2 in enumerate(points[i1 + 1:], start=i1 + 1):
                distance = dist(p1, p2)
                edges[i1].append([distance, i2])
                edges[i2].append([distance, i1])
        heap = edges[0]
        heapify(heap)
        total_cost, seen = 0, {0}
        while len(seen) < N:
            cost, node = heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            total_cost += cost
            for dist, next_ in edges[node]:
                if next_ not in seen:
                    heappush(heap, [dist, next_])
        return total_cost
