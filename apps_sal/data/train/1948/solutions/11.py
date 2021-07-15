class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        res = 1
        for x, y in points:
            order = []
            for x1, y1 in points:
                if x != x1 or y != y1:
                    d = math.sqrt((x1 - x)**2 + (y1 - y)**2)
                    if d <= 2 * r:
                        delta = math.acos(d / (2 * r))
                        angle = math.atan2(y1 - y, x1 - x)
                        order.append((angle - delta, 1))
                        order.append((angle + delta, -1))
            order.sort(key=lambda x: (x[0], -x[1]))
            count = 1
            for _, entry in order:
                count += entry
                res = max(res, count)
        return res
