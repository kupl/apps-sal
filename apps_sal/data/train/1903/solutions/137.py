import heapq


def dist(i, j, points):
    return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.cnt = n

    def find(self, x):
        if self.root[x] == x:
            return x
        p = self.root[x]
        self.root[x] = self.find(p)
        return self.root[x]

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        self.root[ri] = rj
        self.cnt -= 1


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(i, j, points), i, j))

        heapq.heapify(edges)
        res = 0
        uf = UnionFind(n)
        while uf.cnt > 1:
            e = None
            while True:
                e = heapq.heappop(edges)
                if uf.find(e[1]) != uf.find(e[2]):
                    break
            res += e[0]
            uf.union(e[1], e[2])
        return res
