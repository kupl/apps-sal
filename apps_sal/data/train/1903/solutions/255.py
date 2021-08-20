class Node:

    def __init__(self, data, rank, node):
        self.data = data
        self.rank = rank
        self.node = node
        self.parent = self


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def findManhattanDistance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        edges = []
        for (i, p1) in enumerate(points):
            for j in range(i + 1, len(points)):
                edges.append([i, j, findManhattanDistance(p1, points[j])])
        edges = sorted(edges, key=lambda x: x[2])
        N = len(points)
        hashMap = {}
        for i in range(N):
            node = Node(i, 0, None)
            hashMap[node.data] = node

        def Union(data1, data2):
            node1 = hashMap[data1]
            node2 = hashMap[data2]
            p1 = findSet(node1)
            p2 = findSet(node2)
            if p1 == p2:
                return False
            if p1.rank > p2.rank:
                p1.rank = p1.rank + p2.rank
                p2.parent = p1
            else:
                p2.rank = p2.rank + p1.rank
                p1.parent = p2
            return True

        def findSet(node):
            while node.parent != node:
                node.parent = node.parent.parent
                node = node.parent
            return node.parent
        edge_count = 0
        costs = 0
        for (u, v, w) in edges:
            if Union(u, v):
                costs += w
                edge_count += 1
            if edge_count == N - 1:
                break
        return costs
