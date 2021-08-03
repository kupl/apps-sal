# awice
class DSU:
    def __init__(self, N):
        self.parents = list(range(N))
        self.sz = [1] * N

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.sz[pv] > self.sz[pu]:
            pu, pv = pv, pu
        self.parents[pv] = pu
        self.sz[pu] += self.sz[pv]
        self.sz[pv] = self.sz[pu]

        return True

    def get_sz(self, u):
        return self.sz[self.find(u)]


class Solution:
    # weight edges with full link weighted 2?
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # union find
        alice, bob, full = [], [], []

        for e in edges:
            u, v = e[1] - 1, e[2] - 1
            if e[0] == 1:
                alice.append([u, v])
            elif e[0] == 2:
                bob.append([u, v])
            else:
                full.append([u, v])

        res = 0
        dsua, dsub = DSU(n), DSU(n)
        for u, v in full:
            dsua.union(u, v)
            if not dsub.union(u, v):
                res += 1

        for u, v in alice:
            if not dsua.union(u, v):
                res += 1
        for u, v in bob:
            if not dsub.union(u, v):
                res += 1

        if dsua.get_sz(0) != n or dsub.get_sz(0) != n:
            return -1
        return res
