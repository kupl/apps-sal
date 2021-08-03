class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        self.count -= 1
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        heapq.heapify(edges)
        res = 0
        ds = DSU(n)
        while edges and ds.count != 1:
            cost, u, v = heapq.heappop(edges)
            if ds.union(u, v):
                res += cost
        return res
