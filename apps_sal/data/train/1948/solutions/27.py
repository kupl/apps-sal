class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def valid(x1, y1, x2, y2, r):
            L = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
            if 2 * r < L:
                return False
            else:
                return True

        def getcenter(x1, y1, x2, y2, r):
            L = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
            if r**2 - (L / 2)**2 < 0:
                return None
            d = math.sqrt(r**2 - (L / 2)**2)
            a, b = d * (y1 - y2) / L, d * (x2 - x1) / L
            midx = (x1 + x2) * 0.5
            midy = (y1 + y2) * 0.5
            return midx + a, midy + b, midx - a, midy - b

        def check(x, y, r):
            count = 0
            for u in points:
                if (u[0] - x)**2 + (u[1] - y)**2 <= r**2 + 0.001:
                    count += 1
            return count
        L = len(points)
        if L <= 1:
            return L
        ans = 1
        for i in range(L - 1):
            for j in range(i + 1, L):
                if valid(points[i][0], points[i][1], points[j][0], points[j][1], r):
                    cx1, cy1, cx2, cy2 = getcenter(points[i][0], points[i][1], points[j][0], points[j][1], r)
                    print(cx1, cy1, cx2, cy2)
                    ans = max(ans, check(cx1, cy1, r))
                    ans = max(ans, check(cx2, cy2, r))
        return ans
