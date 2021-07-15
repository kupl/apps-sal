from math import sqrt

class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:

        n = len(points)
        if n <= 2:
            return n

        best = 1

        rr = r ** 2
        for i in range(n):
            for j in range(i + 1, n):
                [x1, y1] = points[i]
                [x2, y2] = points[j]

                xm = (x1 + x2) / 2
                ym = (y1 + y2) / 2

                q = sqrt((x2 - x1)**2 + (y2 - y1)**2)
                qq = (q / 2)**2
                rq = rr - qq
                if rq < 0:
                    continue

                xc = xm + sqrt(rq) * (y1 - y2) / q
                yc = ym + sqrt(rq) * (x2 - x1) / q

                curr = 2
                for k in range(n):
                    if k == i or k == j:
                        continue

                    [x, y] = points[k]
                    if sqrt((x - xc)**2 + (y - yc)**2) <= r:
                        curr += 1

                best = max(best, curr)

        return best




