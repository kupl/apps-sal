class UF:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        self.size[rx] += self.size[ry]
        self.size[ry] = self.size[rx]
        return True

    def sizee(self, x):
        return self.size[self.find(x)]


class Solution:
    def maxNumEdgesToRemove(self, N: int, edges: List[List[int]]) -> int:
        for i in range(len(edges)):
            edges[i][1] -= 1
            edges[i][2] -= 1

        alice = []
        bob = []
        both = []
        for t, u, v in edges:
            if t == 1:
                alice.append([u, v])
            elif t == 2:
                bob.append([u, v])
            else:
                both.append([u, v])

        uf1 = UF(N)
        uf2 = UF(N)
        res = 0
        for u, v in both:
            res += not uf1.union(u, v)
            uf2.union(u, v)
        for u, v in alice:
            res += not uf1.union(u, v)
        for u, v in bob:
            res += not uf2.union(u, v)

        if uf1.sizee(0) != N or uf2.sizee(0) != N:
            return -1
        return res
