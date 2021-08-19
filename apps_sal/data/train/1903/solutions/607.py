class DSU:

    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        r1 = self.find(x)
        r2 = self.find(y)
        if r1 != r2:
            self.p[r1] = r2
            return True
        return False


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dsu = DSU(len(points))

        def getDistance(point1, point2):
            (x1, y1) = point1
            (x2, y2) = point2
            return abs(x1 - x2) + abs(y1 - y2)
        paths = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dis = getDistance(points[i], points[j])
                paths.append((dis, i, j))
        paths.sort()
        cost = 0
        for (dis, i, j) in paths:
            if dsu.union(i, j):
                cost += dis
        return cost
