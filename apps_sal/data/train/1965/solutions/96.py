class UnionFind:
    def __init__(self, n):
        self.par = list(range(n + 1))
        self.sz = list(range(n + 1))

    def find(self, i):
        while i != self.par[i]:
            i = self.par[i]
        return i

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return 0
        if self.sz[x] < self.sz[y]:
            x, y = y, x
        self.par[y] = x
        self.sz[x] += self.sz[y]
        return 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges = sorted(edges, key=lambda x: -x[0])
        uf = UnionFind(n)
        res = e1 = e2 = 0
        for t, u, v in edges:
            if t == 3:
                if uf.union(u, v):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        p0 = uf.par[:]
        for t, u, v in edges:
            if t == 2:
                if uf.union(u, v):
                    e2 += 1
                else:
                    res += 1
        uf.par = p0
        for t, u, v in edges:
            if t == 1:
                if uf.union(u, v):
                    e1 += 1
                else:
                    res += 1
        return res if e1 == e2 == n - 1 else -1
