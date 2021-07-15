
   #     if Nr < Nc:
   #         points = [[c, r] for (r, c) in points]
   #         return self.minAreaRect(points)

from collections import defaultdict
class Solution:
    def minAreaRect(self, points):
        X = list(zip(*points))
        Nr, Nc = len(set(X[0])), len(set(X[1]))
        if Nr == 1 or Nc == 1: return 0

        points.sort()
        columns = defaultdict(list)
        for r, c in points:
            columns[r].append(c)
        ans, lastc = float('inf'), dict()
        for r, cols in columns.items():
            for i, c1 in enumerate(cols):
                for c2 in cols[i+1:]:
                    if (c1, c2) in lastc:
                        area = (r - lastc[(c1, c2)]) * (c2 - c1)
                        #ans = min(ans, area)
                        if area < ans: ans = area
                    lastc[(c1, c2)] = r
        return ans if ans < float('inf') else 0
