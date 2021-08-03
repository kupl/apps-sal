class DJSet:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.par[py] = px
        self.size[px] += self.size[py]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        a = []

        for i in range(n):
            for j in range(i + 1, n):
                a.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))

        a.sort()

        ans = 0
        djSet = DJSet(n)
        for (v, i, j) in a:
            if djSet.union(i, j):
                ans += v

        return ans
