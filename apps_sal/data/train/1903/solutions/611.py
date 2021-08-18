class Union:
    def __init__(self, n):
        self.components = n
        self.parent = [i for i in range(n)]

    def find(self, i):
        if(i != self.parent[i]):
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def _union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if(x != y):
            self.parent[x] = y
            self.components -= 1
            return True
        return False


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = []
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph.append([i, j, d])

        graph = sorted(graph, key=lambda x: x[2])

        k = len(graph)
        if k == 0:
            return 0
        elif k == 1:
            return graph[0][2]

        x = Union(k)
        result = 0
        for i in range(k):
            if x._union(graph[i][0], graph[i][1]):
                result += graph[i][2]
            if x.components == 1:
                return result
        return result
