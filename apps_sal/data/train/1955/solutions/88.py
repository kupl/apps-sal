class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        class UF:

            def __init__(self, n):
                self.p = list(range(n))
                self.sizes = [0 for i in range(n)]

            def union(self, x, y):
                x = self.find(x)
                y = self.find(y)
                if x == y:
                    return
                if self.sizes[x] < self.sizes[y]:
                    (x, y) = (y, x)
                self.p[y] = x
                self.sizes[x] += self.sizes[y]

            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]
        uf = UF(len(s))
        for (x, y) in pairs:
            uf.union(x, y)
        m = defaultdict(list)
        for i in range(len(s)):
            m[uf.find(i)].append(s[i])
        for k in list(m.keys()):
            m[k].sort(reverse=True)
        res = []
        for i in range(len(s)):
            res.append(m[uf.find(i)].pop())
        return ''.join(res)
