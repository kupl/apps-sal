class DisjointSet:
    def __init__(self, n):
        self._parent = [i for i in range(n)]
        self._count = [1 for _ in range(n)]

    def parent(self, i):
        p = i
        while self._parent[p] != p:
            p = self._parent[p]
        self._parent[i] = p
        return p

    def count(self, i):
        return self._count[self.parent(i)]

    def merge(self, i, j):
        pi = self.parent(i)
        pj = self.parent(j)

        if pi == pj:
            return False
        ci, cj = self._count[pi], self._count[pj]
        if ci <= cj:
            self._parent[j] = self._parent[pj] = pi
            self._count[pi] += self._count[pj]
            self._count[pj] = 0
        else:
            self._parent[i] = self._parent[pi] = pj
            self._count[pj] += self._count[pi]
            self._count[pi] = 0
        return True

    def clone(self):
        other = DisjointSet(len(self._parent))
        other._parent = [p for p in self._parent]
        other._count = [c for c in self._count]
        return other


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges_deleted = 0
        dsA = DisjointSet(n)
        for edge_type, u, v in edges:
            ui, vi = u - 1, v - 1
            if edge_type == 3:
                if not dsA.merge(ui, vi):
                    edges_deleted += 1

        dsB = dsA.clone()

        for edge_type, u, v in edges:
            ui, vi = u - 1, v - 1
            if edge_type == 1:
                if not dsA.merge(ui, vi):
                    edges_deleted += 1

        if sum(c > 0 for c in dsA._count) != 1:
            return -1

        for edge_type, u, v in edges:
            ui, vi = u - 1, v - 1
            if edge_type == 2:
                if not dsB.merge(ui, vi):
                    edges_deleted += 1

        if sum(c > 0 for c in dsB._count) != 1:
            return -1

        return edges_deleted
