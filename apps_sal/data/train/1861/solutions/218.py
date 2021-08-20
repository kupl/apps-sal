class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        area = float(inf)
        dt = set()
        for (x, y) in points:
            dt.add((x, y))
        for i in range(len(points)):
            (x, y) = points[i]
            for j in range(i + 1, len(points)):
                (h, v) = points[j]
                if h == x or v == y:
                    continue
                if (x, v) in dt and (h, y) in dt:
                    area = min(area, abs(y - v) * abs(h - x))
        return area if area != float('inf') else 0
