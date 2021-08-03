class DSU:
    def __init__(self, N):
        self.sz = [1] * N
        self.par = list(range(N))

    def find(self, v):
        if self.par[v] != v:
            self.par[v] = self.find(self.par[v])
        return self.par[v]

    def union(self, u, v):
        px = self.find(u)
        py = self.find(v)
        if px == py:
            return False
        if self.sz[px] < self.sz[py]:
            px, py = py, px
        self.par[py] = px
        self.sz[px] += self.sz[py]
        return True

    def size(self, x):
        return self.sz[self.find(x)]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []
        dsu = DSU(N)
        for i in range(N):
            for j in range(i + 1, N):
                d = abs(points[i][0] - points[j][0])
                d += abs(points[i][1] - points[j][1])
                edges.append([i, j, d])
        edges.sort(key=lambda key: key[2])
        ans = 0
        for u, v, d in edges:
            if dsu.union(u, v):
                ans += d
        return ans
