class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        eps = 1e-9

        ret = 1
        n = len(points)
        if n == 1:
            return ret

        points.sort()

        def isect(x1, y1, x2, y2):
            dx2 = (x2 - x1) ** 2
            dy2 = (y2 - y1) ** 2
            if dx2 + dy2 > 4 * r * r:
                return []
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2
            if dx2 + dy2 == 4 * r * r:
                return [(cx, cy)]
            ss2 = (dx2 + dy2) / 4
            ol = math.sqrt(r ** 2 - ss2)
            diffx = ol * math.sqrt(dy2 / (dx2 + dy2))
            diffy = ol * math.sqrt(dx2 / (dx2 + dy2))
            return [(cx - diffx, cy + diffy), (cx + diffx, cy - diffy)]

        for i in range(n - 1):
            a, b = points[i]
            for j in range(i + 1, n):
                c, d = points[j]
                l = isect(a, b, c, d)
                for x, y in l:
                    cur = 0
                    lb = bisect.bisect_left(points, [x - r - eps, y - r - eps])
                    ub = bisect.bisect_right(points, [x + r + eps, y + r + eps])
                    for k in range(lb, ub):
                        dx = points[k][0] - x
                        dy = points[k][1] - y
                        if dx ** 2 + dy ** 2 <= (r + eps) ** 2:
                            cur += 1
                    ret = max(ret, cur)
        return ret
