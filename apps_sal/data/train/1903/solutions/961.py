class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        self.parents[parent_y] = parent_x

    def connected(self, y, x):
        return self.find(y) == self.find(x)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calculate_distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(points)
        uf = UF(n)
        res = 0

        p = []

        for i in range(n):
            for j in range(n):
                if i != j:
                    p.append((i, j, calculate_distance(points[i][0], points[i][1], points[j][0], points[j][1])))

        p.sort(key=lambda x: x[2])

        for x, y, dist in p:
            if not uf.connected(x, y):
                uf.union(x, y)
                res += dist

        return res
