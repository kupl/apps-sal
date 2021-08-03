class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        def find(cx, cy, r):
            ans = 0
            for x, y in points:
                if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2 + 1e-6:
                    ans += 1
            return ans

        ans = 1
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                deno = (y1 - y2) ** 2 + (x1 - x2) ** 2
                if deno > 4 * r * r:
                    continue
                k = math.sqrt(r * r / deno - 0.25)
                ans = max(ans, max(find((x1 + x2) / 2 + t * (y1 - y2), (y1 + y2) / 2 - t * (x1 - x2), r) for t in (k, -k)))
        return ans
