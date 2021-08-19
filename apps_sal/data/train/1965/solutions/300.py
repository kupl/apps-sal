class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        result = 0
        (s1, s2) = (0, 0)
        uf = UnionFind(n)
        for (t, i, j) in edges:
            if t != 3:
                continue
            if uf.union(i, j) is True:
                result += 1
            else:
                s1 += 1
                s2 += 1
        parent = list(uf.parent)
        for (t, i, j) in edges:
            if t != 1:
                continue
            if uf.union(i, j) is True:
                result += 1
            else:
                s1 += 1
        uf.parent = parent
        for (t, i, j) in edges:
            if t != 2:
                continue
            if uf.union(i, j) is True:
                result += 1
            else:
                s2 += 1
        return result if s1 == s2 == n - 1 else -1


class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        (pi, pj) = (self.find(i), self.find(j))
        if pi == pj:
            return True
        self.parent[pi] = pj
        return False
