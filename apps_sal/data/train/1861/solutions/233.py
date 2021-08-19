from collections import defaultdict


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        dctyx = defaultdict(set)
        dctxy = defaultdict(set)
        xlist = []
        ylist = []
        for (x, y) in points:
            dctyx[y].add(x)
            dctxy[x].add(y)
        ans = inf
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                if not (x1 == x2 or y1 == y2):
                    if y2 in dctxy[x1] and x2 in dctyx[y1]:
                        ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        return ans if ans != inf else 0
