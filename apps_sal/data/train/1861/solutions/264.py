class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        s = set([(x, y) for (x, y) in points])
        res = float('inf')
        for (i, point1) in enumerate(points):
            for j in range(i):
                point2 = points[j]
                (x1, y1) = point1
                (x2, y2) = point2
                if x1 != x2 and y1 != y2 and ((x1, y2) in s) and ((x2, y1) in s):
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))
        return res if res < float('inf') else 0
