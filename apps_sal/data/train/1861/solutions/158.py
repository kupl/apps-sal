class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        points_set = set()
        for (x, y) in points:
            points_set.add((x, y))
        for (x1, y1) in points_set:
            for (x2, y2) in points_set:
                if x1 > x2 and y1 > y2 and ((x1, y2) in points_set) and ((x2, y1) in points_set):
                    area = abs(x1 - x2) * abs(y1 - y2)
                    min_area = min(min_area, area)
        return min_area if min_area < float('inf') else 0
