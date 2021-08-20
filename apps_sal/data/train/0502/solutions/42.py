class DisjointSetUnion:

    def __init__(self):
        self._parent = {}
        self._size = {}

    def union(self, a: int, b: int) -> None:
        (a, b) = (self.find(a), self.find(b))
        if a == b:
            return
        if self._size[a] < self._size[b]:
            (a, b) = (b, a)
        self._parent[b] = a
        self._size[a] += self._size[b]

    def find(self, x: int) -> int:
        if x not in self._parent:
            self._parent[x] = x
            self._size[x] = 1
            return x
        while self._parent[x] != x:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return self._parent[x]

    def size(self, x: int) -> int:
        return self._size[self.find(x)]


class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        dsu = DisjointSetUnion()
        for (u, neighborhood) in enumerate(graph):
            for (v, is_connected) in enumerate(neighborhood):
                if is_connected:
                    dsu.union(u, v)
        parent_count = collections.Counter((dsu.find(u) for u in initial))
        best_index = best_count = -1
        for index in initial:
            count = dsu.size(index) if parent_count[dsu.find(index)] == 1 else 0
            if count > best_count or (count == best_count and index < best_index):
                (best_index, best_count) = (index, count)
        return best_index
