class dsu:

    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n + 1)]

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 1
        self.par[x] = y
        return 0


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        gr1 = collections.defaultdict(list)
        gr2 = collections.defaultdict(list)
        edges1 = []
        edges2 = []
        mp = {1: 1, 2: 1, 3: -1}
        for (typ, x, y) in edges:
            if typ == 3 or typ == 1:
                edges1.append([mp[typ], x, y])
            if typ == 3 or typ == 2:
                edges2.append([mp[typ], x, y])
        edges1.sort()
        edges2.sort()
        dsu1 = dsu(n)
        dsu2 = dsu(n)
        oth1 = oth2 = 0
        res = 0
        for (typ, x, y) in edges1:
            if dsu1.union(x, y):
                if typ != -1:
                    res += 1
                else:
                    oth1 += 1
        for (typ, x, y) in edges2:
            if dsu2.union(x, y):
                if typ != -1:
                    res += 1
                else:
                    oth2 += 1
        count = 0
        for i in range(1, n + 1):
            if i == dsu1.par[i]:
                count += 1
            if i == dsu2.par[i]:
                count += 1
        if count > 2:
            return -1
        return res + min(oth1, oth2)
