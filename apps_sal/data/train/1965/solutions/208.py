class UnionFind:
    def __init__(self, m: int, n: int = None):
        self.rank = collections.Counter()
        if n is None:
            self.parent = [i for i in range(m)]
        else:
            self.parent = {(i, j): (i, j) for i in range(m) for j in range(n)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.rank[py] > self.rank[px]:
            px, py = py, px
        if self.rank[py] == self.rank[px]:
            self.rank[px] += 1
        self.parent[py] = px


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1 = UnionFind(n)
        uf2 = UnionFind(n)
        res = 0
        e1 = e2 = e3 = 0
        for e in edges:
            t, u, v = e[0], e[1] - 1, e[2] - 1
            if t == 3:
                if uf1.find(u) == uf1.find(v):
                    res += 1
                else:
                    uf1.union(u, v)
                    uf2.union(u, v)
                    e3 += 1
        for e in edges:
            t, u, v = e[0], e[1] - 1, e[2] - 1
            if t == 1:
                if uf1.find(u) == uf1.find(v):
                    res += 1
                else:
                    uf1.union(u, v)
                    e1 += 1
            elif t == 2:
                if uf2.find(u) == uf2.find(v):
                    res += 1
                else:
                    uf2.union(u, v)
                    e2 += 1
        total = (n - 1) * 2
        if e3 * 2 + e1 + e2 < total:
            return -1
        return res
