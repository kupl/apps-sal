import heapq
from collections import defaultdict


class DSU():
    def __init__(self, par):
        self.par = par
        self.rank = defaultdict(int)

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rank[xr] > self.rank[yr]:
            self.par[yr] = xr
        elif self.rank[xr] < self.rank[yr]:
            self.par[xr] = yr
        else:
            self.par[xr] = yr
            self.rank[yr] += 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        if len(points) == 1:
            return 0
        edges = []
        heapq.heapify(edges)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heapq.heappush(edges, (dist(points[i], points[j]), points[i], points[j]))

        par = {(x, y): (x, y) for (x, y) in points}
        dsu = DSU(par)

        total_len = 0
        count = 0
        while count < len(points) - 1:
            d, p1, p2 = heapq.heappop(edges)
            if dsu.union(tuple(p1), tuple(p2)):
                total_len += d
                count += 1

        return total_len
