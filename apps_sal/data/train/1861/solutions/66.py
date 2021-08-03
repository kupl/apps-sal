from collections import defaultdict
import sys


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        coordMap = defaultdict(set)
        for x, y in points:
            coordMap[x].add(y)
        xlist = sorted(list(coordMap.keys()))
        ans = sys.maxsize
        for i in range(1, len(xlist)):
            for j in range(len(xlist) - i):
                ylist = coordMap[xlist[j]].intersection(coordMap[xlist[j + i]])
                if len(ylist) < 2:
                    continue
                ylist = sorted(list(ylist))
                idx = min(list(range(len(ylist) - 1)), key=lambda i: ylist[i + 1] - ylist[i])
                h = ylist[idx + 1] - ylist[idx]
                ans = min(ans, (xlist[j + i] - xlist[j]) * h)
        return ans if ans != sys.maxsize else 0
