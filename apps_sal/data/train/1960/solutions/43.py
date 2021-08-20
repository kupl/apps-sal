import bisect


class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm = list(range(1, m + 1))
        res = []
        for e in queries:
            idx = perm.index(e)
            res.append(idx)
            perm = [perm[idx]] + [r for (i, r) in enumerate(perm) if i != idx]
        return res
