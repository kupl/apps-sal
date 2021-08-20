from collections import defaultdict


class Solution:

    def minAreaRect(self, points):
        (d, ans) = (defaultdict(set), float('inf'))
        for (r, c) in points:
            d[r].add(c)
        A = sorted(d.keys())
        for (i, r1) in enumerate(A):
            cols1 = d[r1]
            for r2 in A[i + 1:]:
                cols2 = d[r2]
                s = sorted(cols1 & cols2)
                for (c1, c2) in zip(s[:-1], s[1:]):
                    area = abs((r1 - r2) * (c1 - c2))
                    if area < ans:
                        ans = area
        return ans if ans < float('inf') else 0
