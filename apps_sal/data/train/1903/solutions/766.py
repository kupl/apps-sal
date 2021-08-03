class UF:
    def __init__(self):
        self.ranks = {}
        self.pnts = {}
        self.sz = {}

    def find_make_set(self, x):
        if not x in self.pnts:
            self.pnts[x] = None
            self.ranks[x] = 0
            self.sz[x] = 1

        if self.pnts[x] is None:
            return x

        self.pnts[x] = self.find_make_set(self.pnts[x])
        return self.pnts[x]

    def union(self, x, y):
        ra = self.find_make_set(x)
        rb = self.find_make_set(y)

        if ra == rb:
            return ra

        if self.ranks[ra] > self.ranks[rb]:
            self.pnts[rb] = ra
            self.sz[ra] += self.sz[rb]
            return ra

        self.pnts[ra] = rb
        self.sz[rb] += self.sz[ra]
        if self.ranks[ra] == self.ranks[rb]:
            self.ranks[rb] += 1

        return rb


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        base = 10 ** 7

        n = len(points)

        egs = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                u = points[i]
                v = points[j]

                ua = points[i][0] + base * points[i][1]
                va = points[j][0] + base * points[j][1]

                t = (ua, va), abs(u[0] - v[0]) + abs(u[1] - v[1])
                egs.append(t)

        egs.sort(key=lambda x: x[1])

        uf = UF()
        ans = 0

        for e, w in egs:
            u, v = e
            ru = uf.find_make_set(u)
            rv = uf.find_make_set(v)
            if ru != rv:
                uf.union(u, v)
                ans += w
            else:
                if uf.sz[ru] == n:
                    break

        return ans
