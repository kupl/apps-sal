class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parentx, parenty = self.find(x), self.find(y)
        if parentx == parenty:
            return False
        self.parent[parentx] = parenty
        self.size += 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1, uf2 = UnionFind(n), UnionFind(n)
        res = 0

        for t, u, v in edges:
            if t != 3:
                continue
            if (not uf1.union(u - 1, v - 1)) or not (uf2.union(u - 1, v - 1)):
                res += 1

        for t, u, v in edges:
            if t == 1 and not uf1.union(u - 1, v - 1):
                res += 1
            elif t == 2 and not uf2.union(u - 1, v - 1):
                res += 1

        return res if (uf1.size == n and uf2.size == n) else -1
