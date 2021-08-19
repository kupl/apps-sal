class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parents[py] = px

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = []
        uf = UnionFind(len(points))
        res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    graph.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        graph.sort(key=lambda x: x[2])
        for (i, j, w) in graph:
            if not uf.connected(i, j):
                uf.union(i, j)
                res += w
        return res
