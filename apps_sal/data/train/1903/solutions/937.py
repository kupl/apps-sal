from collections import defaultdict


class Solution:
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
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        summ = 0
        for u, v, weight in result:
            summ += weight
        return summ

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.V = len(points)
        self.graph = []
        for i in range(len(points)):
            for j in range(len(points)):
                md = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                self.graph.append([i, j, md])
        return self.KruskalMST()
