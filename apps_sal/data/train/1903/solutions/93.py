import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def add(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)

        if xRoot == yRoot:
            return

        xRank, yRank = self.rank[xRoot], self.rank[yRoot]

        if xRank < yRank:
            yRoot, xRoot = xRoot, yRoot

        self.parent[yRoot] = xRoot
        self.rank[xRoot] += self.rank[yRoot]

        return


class Solution:
    def dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dsu = UnionFind(len(points))
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((self.dist(points[i], points[j]), i, j))

        heapq.heapify(edges)
        ans = 0
        while edges:
            d, u, v = heapq.heappop(edges)
            if dsu.find(u) != dsu.find(v):
                ans += d
                dsu.union(u, v)

        return ans
