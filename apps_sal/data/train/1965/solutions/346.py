class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            px, py = py, px
        self.parent[px] = py
        if self.rank[px] == self.rank[py]:
            self.rank[py] += 1
        self.count -= 1
        return True

    def united(self):
        return self.count == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: -x[0])
        alice = UnionFind(n)
        bob = UnionFind(n)
        added = 0
        for t, a, b in edges:
            a -= 1
            b -= 1
            if t == 3:
                added += 1 if alice.union(a, b) | bob.union(a, b) else 0
            elif t == 1:
                added += 1 if alice.union(a, b) else 0
            elif t == 2:
                added += 1 if bob.union(a, b) else 0

        return len(edges) - added if alice.united() and bob.united() else -1
