class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        self.parent[px] = py
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, res, pq = len(points), 0, list()
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(pq, (d, i, j))

        uf = UnionFind(n)
        while pq:
            d, i, j = heapq.heappop(pq)
            if uf.union(i, j):
                res += d
        return res
