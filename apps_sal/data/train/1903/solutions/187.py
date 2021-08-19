import heapq


class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]

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
        cost = 0
        curr = 0
        dist = [float('inf')] * n
        explored = set()
        explored.add(0)
        cnt = 1
        while cnt < n:
            u = points[curr]
            for (j, v) in enumerate(points):
                if j in explored:
                    continue
                else:
                    dist[j] = min(dist[j], distance(u, v))
            (min_d, curr) = min(((d, j) for (j, d) in enumerate(dist)))
            explored.add(curr)
            cnt += 1
            dist[curr] = float('inf')
            cost += min_d
        return cost
