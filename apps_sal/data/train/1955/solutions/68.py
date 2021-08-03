from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, s): self.p = [i for i in range(len(s))]

            def union(self, x, y): self.p[self.find(x)] = self.find(y)

            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]
        res, cc, uf = [], defaultdict(list), UF(s)
        for x, y in pairs:
            uf.union(x, y)
        for i, c in enumerate(s):
            cc[uf.find(i)].append(c)
        for cc_id in cc.keys():
            cc[cc_id].sort(reverse=True)
        for i in range(len(s)):
            res.append(cc[uf.find(i)].pop())
        return ''.join(res)
