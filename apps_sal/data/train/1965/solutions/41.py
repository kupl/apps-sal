from typing import List


class Solution:
    def find(self, i):
        if i != self.root[i]:
            self.root[i] = self.find(self.root[i])
        return self.root[i]

    def uni(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return 0
        self.root[x] = y
        return 1

    def maxNumEdgesToRemove(self, n, edges):
        # Union find

        res = e1 = e2 = 0

        # Alice and Bob
        self.root = list(range(n + 1))
        for t, i, j in edges:
            if t == 3:
                if self.uni(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        root0 = self.root[:]

        # only Alice
        for t, i, j in edges:
            if t == 1:
                if self.uni(i, j):
                    e1 += 1
                else:
                    res += 1

        # only Bob
        self.root = root0
        for t, i, j in edges:
            if t == 2:
                if self.uni(i, j):
                    e2 += 1
                else:
                    res += 1

        return res if e1 == e2 == n - 1 else -1
