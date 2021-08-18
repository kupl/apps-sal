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


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        result = 0
        i = 0
        e = 0
        g = Graph(len(points))
        for i in range(len(points) - 1):
            for j in range(i, len(points)):
                a = tuple(points[i])
                b = tuple(points[j])
                g.addEdge(a, b, abs(a[0] - b[0]) + abs(a[1] - b[1]))
        g.graph = sorted(g.graph, key=lambda item: item[2])
        parent = [0] * g.V
        rank = [0] * g.V

        dic = {}
        for i, p in enumerate(points):
            dic[tuple(p)] = i

        for i in range(g.V):
            parent[i] = i
        while e < g.V - 1:
            u, v, w = g.graph[i]
            i = i + 1
            x = g.find(parent, dic[u])
            y = g.find(parent, dic[v])
            if x != y:
                e = e + 1
                result += w
                g.union(parent, rank, x, y)
        return result
