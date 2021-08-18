class Solution:
    def find(self, uf, node):
        if node not in uf:
            uf[node] = node

        while node != uf[node]:
            node = uf[node]

        return node

    def union(self, uf, node1, node2):
        uf[self.find(uf, node1)] = self.find(uf, node2)

    def distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        edges = []
        uf = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append([i, j, self.distance(points[i], points[j])])

        edges = sorted(edges, key=lambda x: x[2])

        for edge in edges:
            point1 = edge[0]
            point2 = edge[1]
            edgeCost = edge[2]

            if self.find(uf, point1) != self.find(uf, point2):
                self.union(uf, point1, point2)
                cost += edgeCost

        return cost
