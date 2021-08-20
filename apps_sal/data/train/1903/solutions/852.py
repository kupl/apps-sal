class UnionFind:

    def __init__(self, n):
        self.size = n
        self.parents = [i for i in range(self.size)]
        self.rank = [1 for _ in range(self.size)]

    def find_parent(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find_parent(self.parents[node])
        return self.parents[node]

    def union(self, a, b):
        parent_a = self.find_parent(a)
        parent_b = self.find_parent(b)
        if parent_a == parent_b:
            return
        if self.rank[parent_a] < self.rank[parent_b]:
            (parent_a, parent_b) = (parent_b, parent_a)
        self.parents[parent_b] = parent_a
        self.rank[parent_a] += self.rank[parent_b]


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def build_graph(points):
            result = []

            def distance(a, b):
                return abs(a[0] - b[0]) + abs(a[1] - b[1])
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    weight = distance(points[i], points[j])
                    result.append((weight, i, j))
            return result
        union_find = UnionFind(len(points))
        graph = build_graph(points)
        graph.sort()
        cost = 0
        for (w, a, b) in graph:
            if union_find.find_parent(a) == union_find.find_parent(b):
                continue
            union_find.union(a, b)
            cost += w
        return cost
