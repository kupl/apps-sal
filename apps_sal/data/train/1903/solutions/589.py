import math


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))

        edges.sort()
        # print(edges)
        union_find = UnionFind(len(points))

        min_sum = 0
        for d, i, j in edges:
            if union_find.union(i, j):
                min_sum += d

        return min_sum


class UnionFind:
    def __init__(self, n):

        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, p):
        root = p
        while(root != self.parent[root]):
            root = self.parent[root]

        node = p
        while(node != self.parent[node]):

            nextNode = self.parent[node]
            self.parent[node] = root
            node = nextNode

        return root

    def union(self, p, q):

        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return False

        if self.size[p_root] < self.size[q_root]:
            self.parent[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.parent[q_root] = p_root
            self.size[p_root] += self.size[q_root]

        return True
