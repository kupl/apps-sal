import heapq


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.maxRank = 1

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
            self.maxRank = max(self.maxRank, self.rank[pa])
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
            self.maxRank = max(self.maxRank, self.rank[pb])

    def find(self, a):
        if self.parent[a] == a:
            return a

        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(u, v):
            dx = abs(u[0] - v[0])
            dy = abs(u[1] - v[1])
            return dx + dy

        n = len(points)
        if n == 1:
            return 0
        if n == 2:
            return distance(points[0], points[1])

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = distance(points[i], points[j])
                edges.append((dist, i, j))
        heapq.heapify(edges)
        cost = 0
        ds = DisjointSet(n)
        while ds.maxRank < n:
            dist, u, v = heapq.heappop(edges)
            if ds.find(u) != ds.find(v):
                cost += dist
                ds.union(u, v)
        return cost
