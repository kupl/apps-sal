class UnionFind:

    def __init__(self, n):
        self.root = [i for i in range(n + 1)]
        self.forests = n

    def unite(self, a, b):
        self.forests -= 1
        self.root[self.find(a)] = self.find(b)

    def find(self, a):
        if self.root[a] != a:
            self.root[a] = self.find(self.root[a])
        return self.root[a]


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        (ufA, ufB) = (UnionFind(n), UnionFind(n))
        edges.sort(key=lambda x: -x[0])
        res = 0
        for (t, a, b) in edges:
            if 3 == t:
                if ufA.find(a) == ufA.find(b) and ufB.find(a) == ufB.find(b):
                    res += 1
                if ufA.find(a) != ufA.find(b):
                    ufA.unite(a, b)
                if ufB.find(a) != ufB.find(b):
                    ufB.unite(a, b)
            elif t == 1:
                if ufA.find(a) == ufA.find(b):
                    res += 1
                else:
                    ufA.unite(a, b)
            elif ufB.find(a) == ufB.find(b):
                res += 1
            else:
                ufB.unite(a, b)
        if ufA.forests > 1 or ufB.forests > 1:
            return -1
        return res
