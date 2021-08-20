from collections import defaultdict


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set()
        for (x, y) in points:
            points_set.add((x, y))
        min_area = float('inf')
        for (x1, y1) in points:
            for (x2, y2) in points:
                if x2 > x1 and y2 > y1:
                    if (x2, y1) in points_set and (x1, y2) in points_set:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        min_area = min(min_area, area)
        return min_area if min_area != float('inf') else 0
