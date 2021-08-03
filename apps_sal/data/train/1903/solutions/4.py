class DisjointSet:
    def __init__(self, n):
        self.parent = [-1] * n  # If a node is root, its parent is the negative size

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            # Path compression
            root = self.find(self.parent[x])
            self.parent[x] = root
            return root

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False

        if self.parent[root_a] > self.parent[root_b]:
            temp = root_a
            root_a = root_b
            root_b = temp

        self.parent[root_a] += self.parent[root_b]
        self.parent[root_b] = root_a
        return True

    def size(self, x):
        root = self.find(x)
        return self.parent[root] * -1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []
        for i, point1 in enumerate(points):
            for j in range(i + 1, len(points)):
                point2 = points[j]
                cost = abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
                edges.append([cost, i, j])

        ans = 0
        edges.sort()
        graph = DisjointSet(len(points))
        for edge in edges:
            if graph.union(edge[1], edge[2]):
                ans += edge[0]

        return ans
