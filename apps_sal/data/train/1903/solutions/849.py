class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += self.rank[yRoot]
        else:
            self.parent[xRoot] = yRoot
            self.rank[yRoot] += self.rank[xRoot]


class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        uf = UnionFind(n)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(edges, (dist, i, j))

        totalCost = 0
        while edges:
            dist, i, j = heappop(edges)
            if uf.find(i) != uf.find(j):
                totalCost += dist
                uf.union(i, j)
        return totalCost
