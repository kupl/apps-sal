from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Edge:
    src: int
    dst: int
    weight: int


@dataclass
class Graph:
    num_nodes: int
    edgelist: list
    parent: list = field(default_factory=list)
    rank: list = field(default_factory=list)

    # minimum spanning tree
    mst: list = field(default_factory=list)

    def FindParent(self, node):
        if self.parent[node] == node:
            return node
        return self.FindParent(self.parent[node])

    def KruskalMST(self):
        self.edgelist.sort(key=lambda Edge: Edge.weight)
        self.parent = [None] * self.num_nodes
        self.rank = [None] * self.num_nodes

        for n in range(self.num_nodes):
            self.parent[n] = n
            self.rank[n] = 0

        for edge in self.edgelist:
            root1 = self.FindParent(edge.src)
            root2 = self.FindParent(edge.dst)

            if root1 != root2:
                self.mst.append(edge)
                if self.rank[root1] < self.rank[root2]:
                    self.parent[root1] = root2
                    self.rank[root2] += 1
                else:
                    self.parent[root2] = root1
                    self.rank[root1] += 1

        ret = 0
        for edge in self.mst:
            ret += edge.weight
        return ret


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append(Edge(i, j, dis))

        g = Graph(n, edges)
        return g.KruskalMST()
