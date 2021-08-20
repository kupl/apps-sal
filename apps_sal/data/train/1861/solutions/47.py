from collections import defaultdict
from itertools import combinations
import sys


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        coordMap = defaultdict(list)
        visited = {}
        for (x, y) in points:
            coordMap[x].append(y)
        ans = sys.maxsize
        for x in sorted(coordMap):
            for (y1, y2) in combinations(sorted(coordMap[x]), 2):
                if (y1, y2) in visited:
                    ans = min(ans, (x - visited[y1, y2]) * abs(y1 - y2))
                visited[y1, y2] = x
        return ans if ans != sys.maxsize else 0
