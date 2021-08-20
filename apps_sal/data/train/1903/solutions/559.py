class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def union(self, x, y):
        (a, b) = (self.find(x), self.find(y))
        if a == b:
            return
        if self.rank[a] > self.rank[b]:
            self.parents[b] = self.parents[a]
            self.rank[a] += self.rank[b]
        else:
            self.parents[a] = self.parents[b]
            self.rank[b] += self.rank[a]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        UF = UnionFind(len(points))
        cost = 0
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                edges.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])
        edges.sort(key=lambda x: x[0])
        for i in range(len(edges)):
            (dist, j, k) = edges[i]
            if UF.find(j) != UF.find(k):
                cost += dist
                UF.union(j, k)
        return cost
