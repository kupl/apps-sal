from collections import defaultdict


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        class UF:

            def __init__(self, n):
                self.p = list(range(n))

            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)

            def find(self, i):
                if self.p[i] != i:
                    self.p[i] = self.find(self.p[i])
                return self.p[i]
        uf = UF(len(s))
        m = defaultdict(list)
        res = []
        for (x, y) in pairs:
            uf.union(x, y)
        for i in range(len(s)):
            m[uf.find(i)].append(s[i])
        for key_name in list(m.keys()):
            m[key_name].sort(reverse=True)
        for i in range(len(s)):
            res.append(m[uf.find(i)].pop())
        return ''.join(res)
