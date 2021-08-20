from collections import defaultdict
from heapq import *


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for (i, (x, y)) in enumerate(points):
            for (j, (h, k)) in enumerate(points):
                if j <= i:
                    continue
                d = abs(x - h) + abs(y - k)
                edges.append((i, j, d))
        g = defaultdict(list)
        for e in edges:
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        q = []
        cost = 0
        seen = set()
        heappush(q, (0, 0))
        for _ in range(n):
            while True:
                (w, u) = heappop(q)
                if u in seen:
                    continue
                cost += w
                seen.add(u)
                for (v, w) in g[u]:
                    if v in seen:
                        continue
                    heappush(q, (w, v))
                break
        return cost
