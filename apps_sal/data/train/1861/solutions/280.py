from collections import defaultdict


class Solution:

    def minAreaRect(self, points):
        X = list(zip(*points))
        if len(set(X[0])) == 1 or len(set(X[1])) == 1:
            return 0
        (d, ans) = (defaultdict(set), float('inf'))
        for (r, c) in points:
            d[r].add(c)
        A = list(d.keys())
        for (i, r1) in enumerate(A):
            cols1 = d[r1]
            for r2 in A[i + 1:]:
                cols2 = d[r2]
                s = sorted(cols1 & cols2)
                for (c1, c2) in zip(s[:-1], s[1:]):
                    area = abs((r1 - r2) * (c1 - c2))
                    ans = min(ans, area)
        return ans if ans < float('inf') else 0
