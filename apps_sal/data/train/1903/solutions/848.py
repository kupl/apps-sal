class DSU:

    def __init__(self):
        self.parents = {}

    def makeSet(self, x):
        self.parents[x] = x

    def find(self, x):
        if x not in self.parents:
            self.makeSet(x)
        elif x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.parents[xroot] = yroot
            return True
        return False


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        graph = []
        for (node1, point1) in enumerate(points):
            for (node2, point2) in enumerate(points):
                if node1 != node2:
                    graph.append((distance(point1[0], point1[1], point2[0], point2[1]), node1, node2))
        res = 0
        dsu = DSU()
        for (d, u, v) in sorted(graph):
            if len(dsu.parents) == len(points) and len(set((dsu.find(x) for x in dsu.parents))) == 1:
                return res
            if dsu.union(u, v):
                res += d
        return res
