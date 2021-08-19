class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        pointSet = set([tuple(p) for p in points])
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in pointSet and (x2, y1) in pointSet:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))
        if res == float('inf'):
            return 0
        return res
