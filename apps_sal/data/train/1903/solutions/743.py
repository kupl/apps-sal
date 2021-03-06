class DSU:

    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            (xr, yr) = (yr, xr)
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.sz[yr] = self.sz[xr]
        return True


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []
        for i in range(N):
            for j in range(i + 1, N):
                d = abs(points[i][0] - points[j][0])
                d += abs(points[i][1] - points[j][1])
                edges.append([d, i, j])
        edges.sort()
        dsu = DSU(N)
        ans = 0
        for (d, u, v) in edges:
            if dsu.union(u, v):
                ans += d
        return ans
