class UF:

    def __init__(self, n):
        self.f = list(range(n))
        self.cc = [1] * n

    def find(self, x):
        while x != self.f[x]:
            x = self.f[x]
        return x

    def union(self, x, y):
        (fx, fy) = (self.find(x), self.find(y))
        if fx != fy:
            if self.cc[fx] <= self.cc[fy]:
                self.f[fx] = fy
                (self.cc[fx], self.cc[fy]) = (0, self.cc[fx] + self.cc[fy])
            else:
                self.f[fy] = fx
                (self.cc[fx], self.cc[fy]) = (self.cc[fx] + self.cc[fy], 0)


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not s or not pairs:
            return s
        n = len(s)
        uf = UF(n)
        for p in pairs:
            (a, b) = (p[0], p[1])
            uf.union(a, b)
        f2c = collections.defaultdict(list)
        for i in range(n):
            f = uf.find(i)
            f2c[f].append(i)
        ls = [''] * n
        for (_, comp) in list(f2c.items()):
            if not comp:
                continue
            tmp = [s[c] for c in comp]
            comp.sort()
            tmp.sort()
            for i in range(len(comp)):
                ls[comp[i]] = tmp[i]
        return ''.join(ls)
