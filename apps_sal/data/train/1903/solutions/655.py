class Union:

    def __init__(self, vertices):
        self.parent = [i for i in range(vertices)]

    def find(self, i):
        if self.parent[i] != i:
            return self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        self.parent[x] = y


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = Union(n)

        def dist(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        costs = []
        for i in range(n):
            for j in range(n):
                costs.append([i, j, dist(points[i], points[j])])
        costs = sorted(costs, key=lambda x: x[2])
        ans = 0
        i = 0
        s = 0
        while s < n - 1:
            (u, v, cost) = costs[i]
            i += 1
            x = uf.find(u)
            y = uf.find(v)
            if x != y:
                uf.union(x, y)
                s += 1
                ans += cost
        return ans
