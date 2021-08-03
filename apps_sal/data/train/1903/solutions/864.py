class DSU:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        return True


class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        dict = {}
        for index, i in enumerate(A):
            dict[str(i)] = index
        res = 0
        edges = []
        for index, i in enumerate(A):
            for j in A[index + 1:]:
                x = abs(i[0] - j[0]) + abs(i[1] - j[1])
                y = dict.get(str(i))
                z = dict.get(str(j))
                edges.append([x, y, z])
        edges.sort()
        arr = DSU(len(A))
        for i in edges:
            if arr.union(i[1], i[2]):
                res += i[0]
        return res
