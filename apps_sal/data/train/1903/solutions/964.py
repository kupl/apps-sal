class UF:
    @staticmethod
    def init(n):
        return [i for i in range(n)]

    @staticmethod
    def find(parents, i):
        if parents[i] != i:
            parents[i] = UF.find(parents, parents[i])
        return parents[i]

    @staticmethod
    def union(parents, i, j):
        parents[UF.find(parents, i)] = UF.find(parents, j)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []

        n = len(points)
        for i in range(n):
            r1, c1 = points[i]
            for j in range(i + 1, n):
                r2, c2 = points[j]
                distances.append([abs(r1 - r2) + abs(c1 - c2), i, j])
        distances.sort()

        res = 0
        parents = UF.init(n)
        for c, i, j in distances:
            if UF.find(parents, i) != UF.find(parents, j):
                UF.union(parents, i, j)
                res += c

        return res
