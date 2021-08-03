class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:

        n = len(points)
        ans = 1
        for i in range(n - 1):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, n):
                x2, y2 = points[j][0], points[j][1]
                d = (x1 - x2)**2 + (y1 - y2)**2

                if d > 4 * r * r:
                    continue

                cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
                h = math.sqrt(r * r - d / 4)

                if y1 == y2:
                    dx, dy = 0, h

                else:
                    m = -(x1 - x2) / (y1 - y2)
                    dx, dy = h / math.sqrt(1 + m * m), h * m / (math.sqrt(1 + m * m))

                for sign in [1, -1]:
                    count = 0
                    px, py = cx + sign * dx, cy + sign * dy

                    for k, (x, y) in enumerate(points):
                        if (x - px)**2 + (y - py)**2 <= r * r + 1e-7:
                            count += 1
                    ans = max(ans, count)

        return ans
