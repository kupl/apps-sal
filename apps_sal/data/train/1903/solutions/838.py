from itertools import combinations


class DSU:

    def __init__(self, arr):
        self.p = {}
        self.n = 0

    def add(self, u):
        self.p[u] = u
        self.n += 1

    def find(self, u):
        if self.p[u] != u:
            self.p[u] = self.find(self.p[u])
        return self.p[u]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        self.n -= 1


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = DSU([])
        edge = []
        ans = 0
        for i in range(len(points) - 1):
            d.add(tuple(points[i]))
            for j in range(i + 1, len(points)):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edge.append([(points[i], points[j]), dis])
        d.add(tuple(points[-1]))
        edge.sort(key=lambda x: x[1])
        for e in edge:
            if d.find(tuple(e[0][0])) != d.find(tuple(e[0][1])):
                d.union(tuple(e[0][0]), tuple(e[0][1]))
                ans += e[1]
            if d.n == 0:
                break
        return ans
        '\n        comb = list(combinations(points, 2))\n        edges = []\n        ans = 0\n        for c in comb:\n            d = abs(c[0][0]-c[1][0])+abs(c[0][1]-c[1][1])\n            edges.append((c, d))\n        edges.sort(key=lambda x: x[1])\n        s = []\n        for p in points:\n            p = tuple(p)\n            t = set()\n            t.add(p)\n            s.append(t)\n        print(s)\n        for e in edges:\n            u1 = -1\n            u2 = -1\n            for i in range(len(s)):\n                if tuple(e[0][0]) in s[i]:\n                    u1 = i\n                if tuple(e[0][1]) in s[i]:\n                    u2 = i\n            if u1 != u2:\n                s[u1] = s[u1] | s[u2]\n                s.pop(u2)\n                ans += e[1]\n        return ans\n        '
