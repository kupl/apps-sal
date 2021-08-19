class DSU:

    def __init__(self):
        self.parent = {}
        self.size = {}

    def root(self, a):
        tmp = a
        while(self.parent[tmp] != tmp):
            tmp = self.parent[tmp]
            self.parent[tmp] = self.parent[self.parent[tmp]]
        return tmp

    def union(self, a, b):
        if self.root(a) == self.root(b):
            return True
        else:
            if self.size[self.root(a)] >= self.size[self.root(b)]:
                self.size[self.root(a)] += self.size[self.root(b)]
                self.parent[self.root(b)] = self.root(a)
            else:
                self.size[self.root(b)] += self.size[self.root(a)]
                self.parent[self.root(a)] = self.root(b)

            return False

    def add_edge(self, a, b):
        if a not in self.parent:
            self.parent[a] = a
            self.size[a] = 1
        if b not in self.parent:
            self.parent[b] = b
            self.size[b] = 1

        return self.union(a, b)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # Standard minimum spanning tree

        n = len(points)
        edges = []

        def manhattan_dis(x1, y1, x2, y2): return abs(abs(x1 - x2) + abs(y1 - y2))

        for i in range(n):
            x, y = points[i]
            for j in range(i + 1, n):
                u, v = points[j]
                edges.append(((x, y), (u, v), manhattan_dis(x, y, u, v)))

        edges.sort(key=lambda x: x[2])

        graph = DSU()

        cost = 0

        for edge in edges:
            u, v, wt = edge
            if (not graph.add_edge(u, v)):
                cost += wt

        # print(edges)
        return cost
