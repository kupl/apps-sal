class Dsu:
    def __init__(self, n):
        self.roots = list(range(n + 1))
        self.cnts = [1] * (n + 1)

    def find(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if self.cnts[rx] >= self.cnts[ry]:
            self.roots[ry] = rx
            self.cnts[rx] += self.cnts[ry]
            self.cnts[ry] = 0
        else:
            self.roots[rx] = ry
            self.cnts[ry] += self.cnts[rx]
            self.cnts[rx] = 0
        return True


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsu_alice = Dsu(n)
        dsu_bob = Dsu(n)
        rm = 0
        for t, u, v in edges:
            if t == 3:
                dsu_alice.union(u, v)
                if not dsu_bob.union(u, v):
                    rm += 1

        for t, u, v in edges:
            if t == 1:
                if not dsu_alice.union(u, v):
                    rm += 1
            elif t == 2:
                if not dsu_bob.union(u, v):
                    rm += 1

        if dsu_alice.cnts[dsu_alice.find(1)] != n or dsu_bob.cnts[dsu_bob.find(1)] != n:
            return -1
        return rm
