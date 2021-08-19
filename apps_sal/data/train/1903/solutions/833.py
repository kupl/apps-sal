class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []
        for i in range(N):
            for j in range(i + 1, N):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([dist, i, j])
        edges.sort()
        dsu = DSU()
        ans = 0
        for (u, v, x) in edges:
            if dsu.union(v, x):
                ans += u
        return ans


class DSU:

    def __init__(self):
        self.mp = {}
        self.par = []
        self.sz = []

    def find(self, x):
        try:
            i = self.mp[x]
        except:
            self.mp[x] = i = len(self.mp)
            self.par.append(i)
            self.sz.append(1)
        return self._find(i)

    def _find(self, x):
        if self.par[x] != x:
            self.par[x] = self._find(self.par[x])
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
