class UnionFind(object):
    def __init__(self, n, recursion = False):
        self._par = list(range(n))
        self._size = [1] * n
        self._recursion = recursion

    def root(self, k):
        if self._recursion:
            if k == self._par[k]:
                return k
            self._par[k] = self.root(self._par[k])
            return self._par[k]
        else:
            root = k
            while root != self._par[root]: root = self._par[root]
            while k != root: k, self._par[k] = self._par[k], root
            return root

    def unite(self, i, j):
        i, j = self.root(i), self.root(j)
        if i == j: return False
        if self._size[i] < self._size[j]: i, j = j, i
        self._par[j] = i
        self._size[i] += self._size[j]
        return True

    def is_connected(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, k):
        return self._size[self.root(k)]

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1 = UnionFind(n)
        uf2 = UnionFind(n)
        ans = 0
        
        for i, u, v in edges:
            if i == 3:
                ans += 1 - uf1.unite(u - 1, v - 1)
                uf2.unite(u - 1, v - 1)
        
        for i, u, v in edges:
            if i == 1:
                ans += 1 - uf1.unite(u - 1, v - 1)
            elif i == 2:
                ans += 1 - uf2.unite(u - 1, v - 1)
        
        if uf1.size(0) == uf2.size(0) == n:
            return ans
        else:
            return -1
