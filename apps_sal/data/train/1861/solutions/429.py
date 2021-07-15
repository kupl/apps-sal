from collections import defaultdict
from bisect import insort
class Solution:
    def minAreaRect(self, points):
       # setr, setc = set(), set()
       # for r, c in points:
       #     setr.add(r)
       #     setc.add(c)
       # if len(points) in (len(setr), len(setc)): return 0
        
        points.sort()
        columns = defaultdict(list)
        for r, c in points:
            insort(columns[r], c)
        ans, lastc = float('inf'), dict()
        for r, cols in list(columns.items()):
            #cols = sorted(columns[r])
            for j, y2 in enumerate(cols):
                for i, y1 in enumerate(cols[:j]):
                    if (y1, y2) in lastc:
                        ans = min(ans, (r - lastc[(y1, y2)]) * (y2 - y1))
                    lastc[(y1, y2)] = r
        return ans if ans < float('inf') else 0

