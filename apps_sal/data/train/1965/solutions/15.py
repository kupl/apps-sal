class DSU:

    def __init__(self, n):
        self.p = [-1] * (n + 1)
        self.r = [0] * (n + 1)

    def find_parent(self, x):
        if self.p[x] == -1:
            return x
        self.p[x] = self.find_parent(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa = self.find_parent(a)
        pb = self.find_parent(b)
        if pa == pb:
            return False
        if self.r[pa] <= self.r[pb]:
            self.p[pb] = pa
            self.r[pa] += 1
        else:
            self.p[pa] = pb
            self.r[pb] += 1
        return True


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges = sorted(edges, key=lambda x: -x[0])
        dsu_alice = DSU(n)
        dsu_bob = DSU(n)
        res = 0
        for e in edges:
            if e[0] == 3:
                au = dsu_alice.union(e[1], e[2])
                bu = dsu_bob.union(e[1], e[2])
                if not au and (not bu):
                    res += 1
            elif e[0] == 1:
                if not dsu_alice.union(e[1], e[2]):
                    res += 1
            elif not dsu_bob.union(e[1], e[2]):
                res += 1
        ap = 0
        bp = 0
        for i in range(1, n + 1):
            if ap and dsu_alice.find_parent(i) != ap:
                return -1
            else:
                ap = dsu_alice.find_parent(i)
            if bp and dsu_bob.find_parent(i) != bp:
                return -1
            else:
                bp = dsu_bob.find_parent(i)
        return res
