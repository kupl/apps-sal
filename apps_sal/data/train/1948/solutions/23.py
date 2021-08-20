import math
from decimal import Decimal as D


class Solution:

    def numPoints(self, points: List[List[int]], r: int) -> int:

        def circles_from_p1p2r(p1, p2, r):
            ((x1, y1), (x2, y2)) = (p1, p2)
            (dx, dy) = (x2 - x1, y2 - y1)
            q = math.sqrt(dx ** 2 + dy ** 2)
            if q > 2.0 * r:
                return []
            (x3, y3) = ((x1 + x2) / 2, (y1 + y2) / 2)
            d = math.sqrt(r ** 2 - (q / 2) ** 2)
            c1 = [x3 - d * dy / q, y3 + d * dx / q]
            c2 = [x3 + d * dy / q, y3 - d * dx / q]
            return [c1, c2]
        res = 0
        n = len(points)
        for p in range(n):
            for q in range(p + 1, n):
                TwoCirs = circles_from_p1p2r(points[p], points[q], r)
                for center in TwoCirs:
                    cnt = 0
                    for dots in points:
                        if (dots[0] - center[0]) ** 2 + (dots[1] - center[1]) ** 2 <= r ** 2 + 10 ** (-6):
                            cnt += 1
                    res = max(res, cnt)
        return res if res else 1
