class dsu:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu = self.parents[u]
        pv = self.parents[v]
        if pu != pv:
            if self.rank[pu] < self.rank[pv]:
                self.parents[pu] = pv
            elif self.rank[pu] > self.rank[pv]:
                self.parents[pv] = pu
            else:
                self.parents[pu] = pv
                self.rank[pv] += 1


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def get_dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        h = []
        n = len(points)
        uf = dsu(n)
        for i in range(n):
            for j in range(i):
                heapq.heappush(h, (get_dist(i, j), i, j))
        cost = 0
        count = 0
        while h:
            (c, u, v) = heapq.heappop(h)
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                cost += c
                count += 1
            if count >= n - 1:
                break
        return cost
