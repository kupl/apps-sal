from collections import defaultdict


class Solution:
    def minAreaRect(self, points):
        d = defaultdict(set)
        rset, cset, N, ans = set(), set(), len(points), float('inf')
        for r, c in points:
            rset.add(r)
            cset.add(c)
        Nr, Nc = len(rset), len(cset)
        if Nr == 1 or Nc == 1:
            return 0
        elif Nr < Nc:
            for r, c in points:
                d[r].add(c)
        else:
            for r, c in points:
                d[c].add(r)

        A = sorted(d.keys())
        for i, r1 in enumerate(A):
            cols1 = d[r1]
            for r2 in A[i + 1:]:
                cols2 = d[r2]
                s = sorted(cols1 & cols2)
                for c1, c2 in zip(s[:-1], s[1:]):
                    area = abs((r1 - r2) * (c1 - c2))
                    ans = min(ans, area)
        return ans if ans < float('inf') else 0
