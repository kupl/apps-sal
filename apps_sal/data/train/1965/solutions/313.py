from copy import deepcopy


class DSU:

    def __init__(self, n):
        self.dsu = [i for i in range(n + 1)]

    def find(self, x):
        if x == self.dsu[x]:
            return x
        self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.dsu[yr] = xr
        return


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = []
        bob = []
        both = []
        for (t, x, y) in edges:
            if t == 1:
                alice.append((x, y))
            elif t == 2:
                bob.append((x, y))
            else:
                both.append((x, y))
        dsu = DSU(n)
        counter3 = 0
        for (x, y) in both:
            if dsu.find(x) == dsu.find(y):
                continue
            dsu.union(x, y)
            counter3 += 1
        dsu1 = deepcopy(dsu)
        counter1 = 0
        for (x, y) in alice:
            if dsu1.find(x) == dsu1.find(y):
                continue
            dsu1.union(x, y)
            counter1 += 1
        dsu2 = deepcopy(dsu)
        counter2 = 0
        for (x, y) in bob:
            if dsu2.find(x) == dsu2.find(y):
                continue
            dsu2.union(x, y)
            counter2 += 1
        if counter1 + counter3 != n - 1 or counter2 + counter3 != n - 1:
            return -1
        else:
            return len(edges) + counter3 - 2 * n + 2
