class UnionFind:

    def __init__(self):
        self._parent = {}
        self._size = {}

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self._size[a] < self._size[b]:
            (a, b) = (b, a)
        self._parent[b] = a
        self._size[a] += self._size[b]
        return True

    def find(self, x):
        if x not in self._parent:
            self._parent[x] = x
            self._size[x] = 1
            return x
        while self._parent[x] != x:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return self._parent[x]

    def size(self, x):
        return self._size[self.find(x)]


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa = UnionFind()
        ufb = UnionFind()
        ufa2 = UnionFind()
        ufb2 = UnionFind()
        count = 0
        for (t, u, v) in edges:
            if t == 1:
                ufa.union(u, v)
            elif t == 2:
                ufb.union(u, v)
            else:
                ufa.union(u, v)
                ufb.union(u, v)
                ufa2.union(u, v)
                count += int(ufb2.union(u, v))
        if ufa.size(1) != n or ufb.size(1) != n:
            return -1
        for (t, u, v) in edges:
            if t == 1:
                count += ufa2.union(u, v)
            elif t == 2:
                count += ufb2.union(u, v)
        return len(edges) - count
