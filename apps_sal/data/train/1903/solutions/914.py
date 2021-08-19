class DSU:

    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            if self.r[p_y] > self.r[p_x]:
                self.p[p_x] = p_y
            else:
                self.p[p_y] = p_x
                if self.r[p_y] == self.r[p_x]:
                    self.r[p_x] += 1
            return True
        return False


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return 0

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        dic = {}
        for i in range(n):
            for j in range(i + 1, n):
                dic[i, j] = dist(points[i], points[j])
        o = sorted(list(dic.items()), key=lambda v: v[1])
        dsu = DSU(n)
        res = 0
        for (pts, cost) in o:
            (p1, p2) = pts
            if dsu.union(p1, p2):
                res += cost
        return res
