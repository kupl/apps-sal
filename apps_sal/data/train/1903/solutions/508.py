class DSU():

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        if self.size[xp] < self.size[yp]:
            xp, yp = yp, xp

        self.size[xp] += self.size[yp]
        self.parent[yp] = xp
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        dsu = DSU(len(points))
        ans = 0
        edges = []
        for i, (xi, yi) in enumerate(points):
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                edges.append((abs(xi - xj) + abs(yi - yj), i, j))

        edges.sort()
        ans = 0
        for d, v1, v2 in edges:
            # print(v1,v2,'a')
            if dsu.find(v1) != dsu.find(v2):
                # print(v1,v2,'j')
                ans += d
                dsu.union(v1, v2)

        # print(dsu.parent)
        return ans
