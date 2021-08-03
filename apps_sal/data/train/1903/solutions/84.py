class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = []
        self.parent = [i for i in range(len(points))]
        cost = 0
        self.N = len(points)

        for i in range(len(points) - 1):
            for j in range(len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph.append([i, j, dist])

        graph = sorted(graph, key=lambda x: x[2])

        for u, v, c in graph:
            if self.union(u, v):
                cost += c
            if self.N == 0:
                break

        return cost

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return False

        if self.parent[parentX] <= self.parent[parentY]:
            self.parent[parentY] = parentX
        else:
            self.parent[parentX] = parentY
        self.N -= 1
        return True

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
