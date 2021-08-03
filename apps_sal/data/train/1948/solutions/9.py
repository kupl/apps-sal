class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:

        def count(x0, y0):
            nonlocal ans

            cnt = 0
            for x, y in points:
                if (x - x0) * (x - x0) + (y - y0) * (y - y0) <= r * r + 1e-6:
                    cnt += 1

            ans = max(ans, cnt)

        n = len(points)
        ans = 1
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x_mid, y_mid = (x1 + x2) / 2, (y1 + y2) / 2
                sq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                d = r * r - sq / 4
                if d < 0:
                    continue
                d = sqrt(d)
                sq = sqrt(sq)
                sin = abs(x1 - x2) / sq
                cos = abs(y1 - y2) / sq
                if (x2 - x1) * (y1 - y2) < 0:
                    cos = -cos
                x0, y0 = x_mid - d * cos, y_mid - d * sin
                count(x0, y0)
                x0, y0 = x_mid + d * cos, y_mid + d * sin
                count(x0, y0)

        return ans
