import itertools


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        ans = 1
        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) / 4.0
            if d <= r * r:
                x0 = (x1 + x2) / 2.0 + (y2 - y1) * (r * r - d) ** 0.5 / (d * 4) ** 0.5
                y0 = (y1 + y2) / 2.0 - (x2 - x1) * (r * r - d) ** 0.5 / (d * 4) ** 0.5
                ans = max(ans, sum((x - x0) ** 2 + (y - y0) ** 2 <= r * r + 0.00001 for x, y in points))
        return ans
