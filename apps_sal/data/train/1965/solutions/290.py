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

        self.graph = sorted(self.graph, key=lambda item: -item[2])

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

        return result


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        try:
            g = Graph(n)
            for t, u, v in edges:
                if t in [1, 3]:
                    g.addEdge(u - 1, v - 1, t)

            uni = set()
            cnt = 0
            res = g.KruskalMST()
            for u, v, t in res:
                if t == 3:
                    uni.add((u, v))
                else:
                    cnt += 1

            g = Graph(n)
            for t, u, v in edges:
                if t in [2, 3]:
                    g.addEdge(u - 1, v - 1, t)

            res = g.KruskalMST()
            for u, v, t in res:
                if t == 3:
                    uni.add((u, v))
                else:
                    cnt += 1
            return len(edges) - len(uni) - cnt
        except:
            return -1
