class UFDS:

    def __init__(self, n):
        self.p = list(range(n))

    def find(self, k):
        if self.p[k] == k:
            return k
        self.p[k] = self.find(self.p[k])
        return self.p[k]

    def issame(self, i, j):
        return self.find(i) == self.find(j)

    def union(self, i, j):
        (pi, pj) = (self.find(i), self.find(j))
        if pi == pj:
            return
        if pi < pj:
            self.p[pj] = pi
        else:
            self.p[pi] = pj


class Solution:

    def minCostConnectPoints(self, A: List[List[int]]) -> int:

        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        n = len(A)
        dists = []
        for i in range(n):
            for j in range(i + 1, n):
                dists.append((dist(A[i], A[j]), (i, j)))
        dists.sort()
        ufds = UFDS(n)
        total = 0
        for (d, (i, j)) in dists:
            if not ufds.issame(i, j):
                total += d
                ufds.union(i, j)
        return total
