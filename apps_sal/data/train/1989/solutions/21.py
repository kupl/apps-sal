class Solution:

    def longestAwesome(self, s: str) -> int:
        p = [0]
        for c in s:
            x = int(c)
            p.append(p[-1])
            p[-1] ^= 1 << x
        first = {}
        valid = {1 << x for x in range(10)}
        valid.add(0)
        res = 0
        for (j, pj) in enumerate(p):
            for target in valid:
                i = first.get(pj ^ target, None)
                if i is not None:
                    res = max(res, j - i)
            first.setdefault(pj, j)
        return res
