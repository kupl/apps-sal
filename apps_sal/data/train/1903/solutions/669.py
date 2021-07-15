
from heapq import *
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        dist = lambda p0, p1: abs(p1[0] - p0[0]) + abs(p1[1] - p0[1])
        q = [(0, 0)]
        nodes = set(range(n))
        res = 0
        while q:
            d, u = heappop(q)
            if u not in nodes:
                continue
            nodes.remove(u)
            res = res + d
            if len(nodes) == 0:
                return res
            for v in nodes:
                w = dist(points[u], points[v])
                heappush(q, (w, v))
