class Ufs:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, a, b):
        aroot = self.find(a)
        broot = self.find(b)
        if aroot == broot:
            return
        if self.rank[aroot] < self.rank[broot]:
            self.p[aroot] = broot
        elif self.rank[aroot] > self.rank[broot]:
            self.p[broot] = aroot
        else:
            self.p[aroot] = broot
            self.rank[broot] += 1

    def connect(self, a, b):
        if self.find(a) == self.find(b):
            return True
        else:
            return False


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calc(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])
        edges = []
        n = len(points)
        vis = {}
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([calc(points[i], points[j]), i, j])
        edges.sort()
        ans = 0
        ufs = Ufs(n)
        cnt = i = 0
        while(cnt < n - 1):
            w, u, v = edges[i]
            i += 1
            if ufs.connect(u, v):
                continue
            ans += w
            ufs.union(u, v)
            cnt += 1
        return ans
