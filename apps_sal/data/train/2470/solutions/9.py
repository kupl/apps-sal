from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        d = {}
        for domi in dominoes:
            p = tuple(sorted(domi))
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        c = 0
        for n in list(d.values()):
            s = n * (n - 1) // 2
            c += s
        return c
