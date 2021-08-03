class DisjointSet():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def ManhattanDistance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x2 - x1) + abs(y2 - y1)

        edges = [(ManhattanDistance(points[i], points[j]), i, j) for i in range(n) for j in range(i + 1, n)]
        edges.sort()

        graph = DisjointSet(n)
        ans = 0
        for cost, u, v in edges:
            if graph.find(u) != graph.find(v):
                graph.union(u, v)
                ans += cost

        return ans
