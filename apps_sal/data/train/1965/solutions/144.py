class unionfindset:
    def __init__(self, n=0):
        self.par = {}
        self.rank = {}
        self.count = n
        for i in range(1, 1 + n):
            self.par[i] = i
            self.rank[i] = 1

    def find(self, u):

        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] < self.rank[pv]:
            self.par[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.par[pv] = pu
        else:
            self.par[pv] = pu
            self.rank[pu] += 1
        self.count -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        unf1 = unionfindset(n)
        unf2 = unionfindset(n)
        out = 0
        for i, u, v in edges:
            if i == 1 or i == 2:
                continue
            if not unf1.union(u, v) or not unf2.union(u, v):
                out += 1

        for i, u, v in edges:
            if i == 1:
                if not unf1.union(u, v):
                    out += 1

            elif i == 2:
                if not unf2.union(u, v):
                    out += 1

        if unf1.count != 1 or unf2.count != 1:
            return -1

        return out
