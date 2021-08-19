class UnionFind:

    def __init__(self, n):
        self.state = [-1] * n
        self.cnt = n

    def root(self, u):
        v = self.state[u]
        if v < 0:
            return u
        self.state[u] = res = self.root(v)
        return res

    def merge(self, u, v):
        ru = self.root(u)
        rv = self.root(v)
        if ru == rv:
            return
        du = self.state[ru]
        dv = self.state[rv]
        if du > dv:
            (ru, rv) = (rv, ru)
        if du == dv:
            self.state[ru] -= 1
        self.state[rv] = ru
        self.cnt -= 1
        return


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        au = UnionFind(n)
        bu = UnionFind(n)
        ee = [[] for _ in range(3)]
        for (t, u, v) in edges:
            ee[t - 1].append((u - 1, v - 1))
        ans = 0
        for (u, v) in ee[2]:
            if au.root(u) == au.root(v):
                ans += 1
                continue
            au.merge(u, v)
            bu.merge(u, v)
        for (u, v) in ee[0]:
            if au.root(u) == au.root(v):
                ans += 1
                continue
            au.merge(u, v)
        for (u, v) in ee[1]:
            if bu.root(u) == bu.root(v):
                ans += 1
                continue
            bu.merge(u, v)
        if au.cnt == 1 and bu.cnt == 1:
            return ans
        else:
            return -1
