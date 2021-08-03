
class UnionFind:
    def __init__(self, n):
        self.groups = list(range(n))

    def find(self, i):
        if self.groups[i] == i:
            return i
        p = self.find(self.groups[i])
        self.groups[i] = p
        return p

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)

        self.groups[pi] = pj


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost_array = []

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                cost_array.append((weight, i, j))
        cost_array.sort()
        res = 0
        uf = UnionFind(len(points))
        for weight, i, j in cost_array:
            if uf.find(i) == uf.find(j):
                continue
            uf.union(i, j)
            res += weight
        return res
