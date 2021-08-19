# Prim's algorithm
from collections import defaultdict
from heapq import *


class Solution:
    def minCostConnectPoints(self, points):
        graph = defaultdict(list)
        n = len(points)
        def dist(p0, p1): return abs(p1[0] - p0[0]) + abs(p1[1] - p0[1])
        for u in range(n):
            for v in range(u + 1, n):
                w = dist(points[u], points[v])
                graph[u].append((v, w))
                graph[v].append((u, w))
        q = [(0, 0)]
        visited = set()
        res = 0
        while q:
            d, u = heappop(q)
            if u in visited:
                continue
            visited.add(u)
            res = res + d
            if len(visited) == n:
                return res
            for v, w in graph[u]:
                if v not in visited:
                    heappush(q, (w, v))
