from copy import deepcopy


class UnionFind:
    def __init__(self, n):
        self.leaders = [i for i in range(n)]
        self.ranks = [1 for i in range(n)]

    def find(self, x):
        # p = x
        # while p != self._leaders[p]:
        #     p = self._leaders[p]
        # while x != p:
        #     self._leaders[x], x = p, self._leaders[x]
        # return p
        if self.leaders[x] != x:
            self.leaders[x] = self.find(self.leaders[x])
        return self.leaders[x]

    def union(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p == q:
            return False
        if self.ranks[p] < self.ranks[q]:
            self.leaders[p] = q
        elif self.ranks[p] > self.ranks[q]:
            self.leaders[q] = p
        else:
            self.leaders[q] = p
            self.ranks[p] += 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        res, cnt1 = 0, 0
        uf1 = UnionFind(n + 1)
        for g, u, v in edges:
            if g == 3:
                if uf1.union(u, v):
                    cnt1 += 1
                else:
                    res += 1

        uf2 = deepcopy(uf1)
        cnt2 = cnt1
        for g, u, v in edges:
            if g == 1:
                if uf1.union(u, v):
                    cnt1 += 1
                else:
                    res += 1

        for g, u, v in edges:
            if g == 2:
                if uf2.union(u, v):
                    cnt2 += 1
                else:
                    res += 1

        if cnt1 != n - 1 or cnt2 != n - 1:
            return -1
        return res
