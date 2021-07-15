class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        m = set()
        for point in points:
            m.add(tuple(point))
        res = 0x3fffffff
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in m and (x2, y1) in m:
                        res = min(res, abs((y1 - y2) * (x1 - x2)))
        res = 0 if res == 0x3fffffff else res
        return res
