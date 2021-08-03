class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = inf = float('inf')
        points_set = set(tuple(i) for i in points)
        points = list(points_set)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2 and (x1, y2) in points_set and (x2, y1) in points_set:
                    res = min(res, abs((x2 - x1) * (y2 - y1)))
        return res if res != inf else 0
