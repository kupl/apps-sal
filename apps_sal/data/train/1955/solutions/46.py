class DSU:

    def __init__(self, n):
        self.parent = list(range(n))

    def getP(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.getP(self.parent[i])
            return self.parent[i]
        else:
            return i

    def rewrire(self):
        tops = set()
        for i in range(len(self.parent)):
            if i != self.parent[i]:
                self.parent[i] = self.getP(i)

    def merge(self, a, b):
        (pa, pb) = (self.getP(a), self.getP(b))
        if pa == pb:
            return
        if pa < pb:
            self.parent[pb] = pa
        else:
            self.parent[pa] = pb

    def connect(self, xs):
        for (a, b) in xs:
            self.merge(a, b)
        self.rewrire()


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = DSU(n)
        uf.connect(pairs)
        group = defaultdict(list)
        for (i, pindex) in enumerate(uf.parent):
            group[pindex].append((s[i], i))
        r = [None] * n
        for (gk, gv) in list(group.items()):
            cxs = []
            ixs = []
            for (c, index) in gv:
                cxs.append(c)
                ixs.append(index)
            cxs.sort()
            ixs.sort()
            for i in range(len(ixs)):
                r[ixs[i]] = cxs[i]
        return ''.join(r)
