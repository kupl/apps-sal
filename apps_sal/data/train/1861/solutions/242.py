MAX_VAL = 10 ** 9 + 7


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        for (x, y) in points:
            points_set.add((x, y))
        n = len(points)
        min_area = MAX_VAL
        for i in range(n - 1):
            for j in range(i + 1, n):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                if x1 != x2 and y1 != y2 and ((x2, y1) in points_set) and ((x1, y2) in points_set):
                    curr_area = abs((x1 - x2) * (y1 - y2))
                    min_area = min(min_area, curr_area)
        return 0 if min_area == MAX_VAL else min_area
