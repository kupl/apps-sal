class Solution:

    def getC(self, p1, p2, r):
        ([x1, y1], [x2, y2]) = (p1, p2)
        dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if dist > 2.0 * r:
            return []
        (x3, y3) = ((x1 + x2) / 2, (y1 + y2) / 2)
        magnitude = sqrt(r ** 2 - (dist / 2) ** 2)
        c1 = [x3 - magnitude * (y1 - y2) / dist, y3 + magnitude * (x1 - x2) / dist]
        c2 = [x3 + magnitude * (y1 - y2) / dist, y3 - magnitude * (x1 - x2) / dist]
        return [c1, c2]

    def numPoints(self, points: List[List[int]], r: int) -> int:
        ans = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                C = self.getC(points[i], points[j], r)
                for c in C:
                    cnt = 0
                    for pt in points:
                        if (pt[0] - c[0]) ** 2 + (pt[1] - c[1]) ** 2 <= r ** 2 + 1e-06:
                            cnt += 1
                    ans = max(ans, cnt)
        return ans if ans else 1
