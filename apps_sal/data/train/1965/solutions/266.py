class UF:

    def __init__(self, N):
        self.N = N
        self.parents = list(range(N))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parents[py] = px
            self.N -= 1
            return True
        return False


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: -x[0])
        used = set()
        uf1 = UF(n)
        for (t, x, y) in edges:
            if t == 3:
                if uf1.union(x - 1, y - 1):
                    used.add((t, x, y))
        for (t, x, y) in edges:
            if t == 1:
                if uf1.union(x - 1, y - 1):
                    used.add((t, x, y))
        uf2 = UF(n)
        for (t, x, y) in edges:
            if t == 3:
                if uf2.union(x - 1, y - 1):
                    used.add((t, x, y))
        for (t, x, y) in edges:
            if t == 2:
                if uf2.union(x - 1, y - 1):
                    used.add((t, x, y))
        if uf1.N > 1 or uf2.N > 1:
            return -1
        return len(edges) - len(used)
