class DisjointSet:
    def __init__(self, size):
        self.size = size
        self.parents = list(range(size))

    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            self.parents[parent1] = parent2
            return True
        return False


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        is_connected = [False] * N
        edges = []
        for i in range(N):
            for j in range(i + 1, N):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance, i, j))
        edges.sort()
        cost = 0
        disjoint_set = DisjointSet(N)
        for distance, i, j in edges:
            if disjoint_set.union(i, j):
                cost += distance
        return cost
