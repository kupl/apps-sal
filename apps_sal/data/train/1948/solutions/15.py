class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        best = 1
        for i in range(len(points)):
            p1 = complex(*points[i])
            for j in range(i + 1, len(points)):
                p2 = complex(*points[j])
                d = abs(p1 - p2)
                if d > 2 * r:
                    continue
                h = math.sqrt(r * r - d * d / 4)
                c = (p1 + p2) / 2 + (p1 - p2) * h / d * 1j

                count = 0
                for x, y in points:
                    if (x - c.real) ** 2 + (y - c.imag) ** 2 <= r ** 2 + 1e-6:
                        count += 1
                best = max(best, count)
        return best
