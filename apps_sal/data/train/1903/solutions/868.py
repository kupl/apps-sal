class Solution(object):
    def minCostConnectPoints(self, points):

        g = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                g.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))

        g0 = sorted(g, key=lambda x: x[2])
        uf = UnionFind(len(points))

        ans = 0
        for x, y, z in g0:
            if uf.union(x, y):
                ans += z

        return ans


class UnionFind():
    def __init__(self, n):
        self.parents = {i: i for i in range(0, n)}
        self.groups = n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        self.parents[y] = x
        self.groups -= 1
        return True
