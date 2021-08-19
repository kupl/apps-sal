from heapq import heappush, heappop


class DSU:

    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            (xr, yr) = (yr, xr)
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.sz[yr] = self.sz[xr]
        return True

    def size(self, x):
        return self.sz[self.find(x)]


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        def weight(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        edges = []
        ans = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heappush(edges, (weight(i, j), i, j))
        uf = DSU(len(points) + 1)
        while edges:
            e = heappop(edges)
            if uf.union(e[1], e[2]):
                ans += e[0]
                if uf.size(e[1]) == len(points):
                    return ans
