from collections import defaultdict


class UnionFind:

    def __init__(self, n: int):
        self.n = list(range(n))

    def root(self, element: int):
        root = self.n[element]
        while root != self.n[root]:
            root = self.n[root]
        temp = self.n[element]
        while temp != self.n[temp]:
            self.n[temp] = root
            temp = self.n[temp]
        return root

    def union(self, a: int, b: int):
        rootA = self.root(a)
        rootB = self.root(b)
        self.n[rootB] = rootA

    def find(self, a: int, b: int):
        return self.root(a) == self.root(b)


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        graph = defaultdict(list)
        edges = []
        for i in range(len(points)):
            (xi, yi) = points[i]
            for j in range(i + 1, len(points)):
                (xj, yj) = points[j]
                edges.append((abs(xi - xj) + abs(yi - yj), i, j))
        edges.sort()
        total = 0
        uf = UnionFind(len(points))
        for (distance, origin, destination) in edges:
            if not uf.find(origin, destination):
                uf.union(origin, destination)
                total += distance
        return total
