class Solution:

    def find(self, x, parent):
        if parent[x] != x:
            parent[x] = self.find(parent[x], parent)
        return parent[x]

    def union(self, x, y, parent):
        (px, py) = (self.find(x, parent), self.find(y, parent))
        parent[py] = px

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = []
        n = len(points)
        for i in range(n):
            parent.append(i)
        edges = []
        for i in range(len(points)):
            (x, y) = points[i]
            for j in range(i + 1, len(points)):
                (u, v) = points[j]
                edges.append([i, j, abs(x - u) + abs(y - v)])
        edges = sorted(edges, key=lambda x: x[2])
        cost = 0
        for i in range(len(edges)):
            (p1, p2, w) = edges[i]
            if self.find(p1, parent) != self.find(p2, parent):
                self.union(p1, p2, parent)
                cost += w
        return cost
