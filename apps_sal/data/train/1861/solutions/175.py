from math import inf


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        N, min_area = len(points), inf
        d = set()
        for i in range(N):
            d.add(tuple(points[i]))
        # print(d)
        for i in range(N):
            for j in range(i + 1, N, 1):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if (x1 > x2 and y1 > y2) or (x2 > x1 and y2 > y1):
                    if (x1, y2) in d and (x2, y1) in d:
                        min_area = min(min_area, (x2 - x1) * (y2 - y1))

        if min_area == inf:
            return 0
        else:
            return min_area
