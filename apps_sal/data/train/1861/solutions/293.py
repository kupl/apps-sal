import sys


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set([(x, y) for x, y in points])
        mini = sys.maxsize
        for i, p1 in enumerate(points):
            for j in range(i):
                p2 = points[j]
                if (p1[0] != p2[0]) and (p1[1] != p2[1]) and (p1[0], p2[1]) in S and (p2[0], p1[1]) in S:
                    mini = min(mini, abs((p1[1] - p2[1]) * (p1[0] - p2[0])))
        return mini if mini != sys.maxsize else 0
