from collections import defaultdict
from itertools import combinations
import sys


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        coordMap = defaultdict(set)
        for x, y in points:
            coordMap[x].add(y)
        ans = sys.maxsize
        for x1, x2 in combinations(list(coordMap.keys()), 2):
            ylist = coordMap[x1].intersection(coordMap[x2])
            if len(ylist) < 2:
                continue
            ylist = sorted(list(ylist))
            idx = min(list(range(len(ylist) - 1)), key=lambda i: ylist[i + 1] - ylist[i])
            h = ylist[idx + 1] - ylist[idx]
            ans = min(ans, (abs(x2 - x1)) * h)
        return ans if ans != sys.maxsize else 0
