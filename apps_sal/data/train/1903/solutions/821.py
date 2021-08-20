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

    def minCostConnectPoints(self, a: List[List[int]]) -> int:
        n = len(a)
        if n == 1:
            return 0
        temp = []
        for i in range(n):
            for j in range(n):
                x = abs(a[i][0] - a[j][0]) + abs(a[i][1] - a[j][1])
                if i != j and i > j:
                    temp.append([x, i, j])
        ans = 0
        temp.sort()
        i = 0
        dsu = DSU(n)
        while dsu.size(0) < n:
            if dsu.find(temp[i][1]) != dsu.find(temp[i][2]):
                dsu.union(temp[i][1], temp[i][2])
                ans += temp[i][0]
            i += 1
        return ans
