from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            (u, v, w) = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        ans = 0
        for (u, v, weight) in result:
            ans += weight
        return ans


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def getCost(x1, x2, y1, y2):
            return abs(x2 - x1) + abs(y2 - y1)
        g = Graph(len(points))
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                g.addEdge(i, j, getCost(points[i][0], points[j][0], points[i][1], points[j][1]))
        return g.KruskalMST()
