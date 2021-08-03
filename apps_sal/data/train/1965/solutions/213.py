class UnionFind():
    def __init__(self):
        self.uf, self.rank, self.size = {}, {}, {}
        self.roots = set()

    def add(self, x):
        if x not in self.uf:
            self.uf[x], self.rank[x], self.size[x] = x, 0, 1
            self.roots.add(x)

    def find(self, x):
        self.add(x)
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.rank[xr] <= self.rank[yr]:
            self.uf[xr] = yr
            self.size[yr] += self.size[xr]
            self.rank[yr] += (self.rank[xr] == self.rank[yr])
            self.roots.discard(xr)
        else:
            self.uf[yr] = xr
            self.size[xr] += self.size[yr]
            self.roots.discard(yr)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        Ga, Gb, Gab = UnionFind(), UnionFind(), UnionFind()
        for x in range(1, n + 1):
            Ga.add(x), Gb.add(x), Gab.add(x)
        for t, x, y in edges:
            if t in (1, 3):
                Ga.union(x, y)
            if t in (2, 3):
                Gb.union(x, y)
            if t == 3:
                Gab.union(x, y)

        if max(len(Ga.roots), len(Gb.roots)) > 1:
            return -1
        c = len(Gab.roots)
        return len(edges) - (n - c + 2 * (c - 1))
