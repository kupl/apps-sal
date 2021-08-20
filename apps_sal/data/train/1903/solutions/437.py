class UnionFind:

    def __init__(self):
        self.parents = {}
        self.sizes = {}

    def findParent(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.sizes[x] = 1
            return x
        if self.parents[x] != x:
            self.parents[x] = self.findParent(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        (rootX, rootY) = (self.findParent(x), self.findParent(y))
        if rootX == rootY:
            return
        if self.sizes[rootX] < self.sizes[rootY]:
            self.sizes[rootY] += self.sizes[rootX]
            self.parents[rootX] = rootY
        else:
            self.sizes[rootX] += self.sizes[rootY]
            self.parents[rootY] = rootX

    def numberOfComponents(self):
        return sum((1 for (x, p) in self.parents.items() if x == p))


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        uf = UnionFind()
        N = len(points)
        edges = []
        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                ([x1, y1], [x2, y2]) = (points[i], points[j])
                edges.append([dist(x1, y1, x2, y2), i, j])
        edges.sort()
        ans = 0
        edgesTaken = 0
        i = 0
        while edgesTaken < N - 1:
            (d, x, y) = edges[i]
            if uf.findParent(x) != uf.findParent(y):
                uf.union(x, y)
                ans += d
                edgesTaken += 1
            i += 1
        return ans
