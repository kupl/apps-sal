class UnionFind(object):

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rnk = [0] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distances = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distances.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])
        distances.sort(key=lambda x: x[2])
        res = 0
        uf = UnionFind(n)
        for (i, j, d) in distances:
            if uf.find(i) == uf.find(j):
                continue
            res += d
            uf.union(i, j)
        return res
