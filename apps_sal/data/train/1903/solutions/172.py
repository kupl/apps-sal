from heapq import *


class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        def dist(p0, p1): return abs(p1[0] - p0[0]) + abs(p1[1] - p0[1])
        q = [(0, 0)]
        visited = set()
        nodes = set(range(len(points)))
        res = 0
        while q:
            d, u = heappop(q)
            if u in visited:
                continue
            visited.add(u)
            res = res + d
            if len(visited) == n:
                return res
            for v in nodes:
                if v not in visited:
                    w = dist(points[u], points[v])
                    heappush(q, (w, v))
