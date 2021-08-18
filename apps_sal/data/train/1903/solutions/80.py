from heapq import heappush, heappop


class UnionFind:
    def __init__(self, n):
        self.group = list(range(n))
        self.size = [0] * n

    def find(self, i):
        if i == self.group[i]:
            return i
        p = self.find(self.group[i])
        self.group[i] = p
        return p

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] <= self.size[j]:
            self.group[i] = j
            self.size[j] += self.size[i]
        else:
            self.group[j] = i
            self.size[i] += self.size[j]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        weights = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(weights, (weight, i, j))

        uf = UnionFind(len(points))
        res = 0

        while weights:
            min_edge, i, j = heappop(weights)
            if uf.find(i) == uf.find(j):
                continue
            uf.union(i, j)
            res += min_edge

        return res
