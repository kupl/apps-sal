class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        point_set = {(x, y) for (x, y) in points}
        min_area = math.inf
        for i in range(n):
            (x0, y0) = points[i]
            for j in range(i + 1, n):
                (x1, y1) = points[j]
                if (x0, y1) in point_set and (x1, y0) in point_set:
                    area = abs(x0 - x1) * abs(y0 - y1)
                    if area > 0:
                        min_area = min(min_area, area)
        return 0 if min_area == math.inf else min_area
