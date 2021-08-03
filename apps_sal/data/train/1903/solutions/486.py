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
        '''
        d = DSU([])
        edge = []
        ans = 0
        for i in range(len(points)-1):
            d.add(tuple(points[i]))
            for j in range(i+1,len(points)):
                dis = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edge.append([(points[i],points[j]), dis])
        d.add(tuple(points[-1]))
        edge.sort(key=lambda x:x[1])
        for e in edge:
            if d.find(tuple(e[0][0])) != d.find(tuple(e[0][1])):
                d.union(tuple(e[0][0]),tuple(e[0][1]))
                ans += e[1]
            if d.n == 0:
                break
        return ans
        '''

        comb = list(combinations(points, 2))
        edges = []
        ans = 0
        for c in comb:
            d = abs(c[0][0] - c[1][0]) + abs(c[0][1] - c[1][1])
            edges.append((c, d))
        edges.sort(key=lambda x: x[1])
        s = []
        for p in points:
            p = tuple(p)
            t = set()
            t.add(p)
            s.append(t)
        print(s)
        for e in edges:
            u1 = -1
            u2 = -1
            for i in range(len(s)):
                if tuple(e[0][0]) in s[i]:
                    u1 = i
                if tuple(e[0][1]) in s[i]:
                    u2 = i
            if u1 != u2:
                s[u1] = s[u1] | s[u2]
                s.pop(u2)
                ans += e[1]
            if len(s) == 1:
                break
        return ans
