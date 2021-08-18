class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        ans = 1
        for x, y in points:
            angles = []
            for x1, y1 in points:
                if (x1 != x or y1 != y) and (d := sqrt((x1 - x)**2 + (y1 - y)**2)) <= 2 * r:
                    angle = atan2(y1 - y, x1 - x)
                    delta = acos(d / (2 * r))
                    angles.append((angle - delta, +1))
                    angles.append((angle + delta, -1))
            angles.sort(key=lambda x: (x[0], -x[1]))
            val = 1
            for _, entry in angles:
                ans = max(ans, val := val + entry)
        return ans
