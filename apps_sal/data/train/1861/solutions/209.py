from collections import defaultdict
from bisect import insort
class Solution:
    def minAreaRect(self, points):
        X = list(zip(*points))
        if len(set(X[0])) == 1 or len(set(X[1])) == 1: return 0 
        points.sort()
        columns = defaultdict(list)
        for r, c in points:
            insort(columns[r], c)
        ans, lastc = float('inf'), dict()
        for r, cols in columns.items():
            for i, c1 in enumerate(cols):
                for c2 in cols[i+1:]:
                    if (c1, c2) in lastc:
                        area = abs((r - lastc[(c1, c2)]) * (c2 - c1))
                        #ans = min(ans, area)
                        if area < ans: ans = area
                    lastc[(c1, c2)] = r
        return ans if ans < float('inf') else 0
