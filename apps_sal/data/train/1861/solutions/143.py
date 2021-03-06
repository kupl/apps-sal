class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        min_area = math.inf
        seen = set()
        for (i, (x0, y0)) in enumerate(points):
            for j in range(i):
                (x1, y1) = points[j]
                if (x0, y1) in seen and (x1, y0) in seen:
                    area = abs(x0 - x1) * abs(y0 - y1)
                    if area > 0:
                        min_area = min(min_area, area)
            seen.add((x0, y0))
        return 0 if min_area == math.inf else min_area
