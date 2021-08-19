class DSU:

    def __init__(self, N):
        self.parents = list(range(N))
        self.ranks = [1] * N
        self.size = 1

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px == py:
            return False
        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[py] > self.ranks[px]:
            self.parents[px] = py
        else:
            self.parents[px] = py
            self.ranks[py] += 1
        self.size += 1
        return True


class Solution:

    def maxNumEdgesToRemove(self, N: int, edges: List[List[int]]) -> int:
        (uf1, uf2, res) = (DSU(N), DSU(N), 0)
        for (t, u, v) in edges:
            if t == 3:
                if not uf1.union(u - 1, v - 1) or not uf2.union(u - 1, v - 1):
                    res += 1
        for (t, u, v) in edges:
            if t == 1 and (not uf1.union(u - 1, v - 1)):
                res += 1
            elif t == 2 and (not uf2.union(u - 1, v - 1)):
                res += 1
        return res if uf1.size == N and uf2.size == N else -1
