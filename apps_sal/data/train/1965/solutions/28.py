class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return px
        if self.rank[px] > self.rank[py]:
            (px, py) = (py, px)
        self.parent[px] = py
        if self.rank[px] == self.rank[py]:
            self.rank[py] += 1


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        both = [(a - 1, b - 1) for (t, a, b) in edges if t == 3]
        alice = [(a - 1, b - 1) for (t, a, b) in edges if t == 1]
        bob = [(a - 1, b - 1) for (t, a, b) in edges if t == 2]
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)
        count = 0
        for (a, b) in both:
            if uf_alice.find(a) != uf_alice.find(b):
                uf_alice.union(a, b)
                uf_bob.union(a, b)
                count += 1
        for (a, b) in alice:
            if uf_alice.find(a) != uf_alice.find(b):
                uf_alice.union(a, b)
                count += 1
        for (a, b) in bob:
            if uf_bob.find(a) != uf_bob.find(b):
                uf_bob.union(a, b)
                count += 1
        p_alice = set([uf_alice.find(i) for i in range(n)])
        if len(p_alice) > 1:
            return -1
        p_bob = set([uf_bob.find(i) for i in range(n)])
        if len(p_bob) > 1:
            return -1
        return len(edges) - count
