class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges = [(t, i - 1, j - 1) for (t, i, j) in edges]
        bob = [-1 for _ in range(n)]
        self.ans = 0
        self.merge(bob, edges, 3)
        alice = bob.copy()
        self.merge(bob, edges, 2)
        self.merge(alice, edges, 1)
        return -1 if min(alice) != -n or min(bob) != -n else self.ans

    def merge(self, par, edges, ty):
        for (t, i, j) in edges:
            if t == ty:
                if self.find(par, i) != self.find(par, j):
                    self.union(par, i, j)
                else:
                    self.ans += 1

    def find(self, par, i):
        if par[i] < 0:
            return i
        par[i] = self.find(par, par[i])
        return par[i]

    def union(self, par, i, j):
        (i, j) = (self.find(par, i), self.find(par, j))
        if i == j:
            return
        if par[j] < par[i]:
            (i, j) = (j, i)
        (par[i], par[j]) = (par[i] + par[j], i)
