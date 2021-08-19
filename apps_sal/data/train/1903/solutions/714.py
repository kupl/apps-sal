class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x] += self.rank[y]
        else:
            self.parent[x] = y
            self.rank[y] += self.rank[x]

    def find(self, i):
        if self.parent[i] == i:
            return self.parent[i]
        return self.find(self.parent[i])


class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        # sort based on cost (i.e. distance)
        edges.sort()
        # using Kruskal's algorithm to find the cost of Minimum Spanning Tree
        res = 0
        uf = UnionFind(n)
        for cost, u, v in edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                res += cost
        return res
