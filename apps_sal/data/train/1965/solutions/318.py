class UnionFind:
    def __init__(self, n):
        self.root = list(range(n + 1))

    def find(self, i):
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return True
        self.root[rx] = ry
        return False


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        if n < 1:
            return 0
        if len(edges) < n - 1:
            return -1
        uf = UnionFind(n)
        ans = e1 = e2 = 0
        for t, u, v in edges:
            if t == 3:
                if uf.union(u, v):
                    ans += 1
                else:
                    e1 += 1
                    e2 += 1
        root_copy = uf.root[:]
        for t, u, v in edges:
            if t == 1:
                if uf.union(u, v):
                    ans += 1
                else:
                    e1 += 1
        uf.root = root_copy
        for t, u, v in edges:
            if t == 2:
                if uf.union(u, v):
                    ans += 1
                else:
                    e2 += 1
        return ans if e1 == e2 == n - 1 else -1
