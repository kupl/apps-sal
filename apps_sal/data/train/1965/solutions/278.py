class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self._count = n

    def find(self, a):
        pa = self.parent[a]
        if pa != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def connect(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False
        self.parent[pa] = pb
        self._count -= 1
        return True

    def counts(self):
        return self._count


class Solution:

    def maxNumEdgesToRemove(self, n, edges):
        edges.sort(reverse=True)
        alice_uf = UnionFind(n)
        bob_uf = UnionFind(n)
        added_edges = 0
        for (t, s, e) in edges:
            if t == 3:
                alice_connected = alice_uf.connect(s, e)
                bob_connected = bob_uf.connect(s, e)
                if alice_connected or bob_connected:
                    added_edges += 1
            if t == 2:
                if bob_uf.connect(s, e):
                    added_edges += 1
            if t == 1:
                if alice_uf.connect(s, e):
                    added_edges += 1
        if alice_uf.counts() == bob_uf.counts() == 1:
            return len(edges) - added_edges
        return -1
