from heapq import heappop, heappush


class DSU:

    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [1] * n
        self.parts = n

    def find(self, a):
        if self.p[a] == a:
            return a
        self.p[a] = self.find(self.p[a])
        return self.p[a]

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        A = self.find(a)
        B = self.find(b)
        if self.rank[A] >= self.rank[B]:
            self.p[B] = A
            self.rank[A] += self.rank[B]
        else:
            self.p[A] = B
            self.rank[B] += self.rank[A]
        return


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dsu = DSU(N)
        pq = []
        for i in range(N):
            (x1, y1) = points[i]
            for j in range(i + 1, N):
                (x2, y2) = points[j]
                heappush(pq, (abs(x1 - x2) + abs(y1 - y2), i, j))
        cost = 0
        while dsu.parts > 1:
            (c, p1, p2) = heappop(pq)
            if dsu.is_connected(p1, p2) == True:
                continue
            dsu.union(p1, p2)
            dsu.parts -= 1
            cost += c
        return cost
