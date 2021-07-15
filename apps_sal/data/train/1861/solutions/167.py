class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple,points))
        min_area = float('inf')
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[:i]:
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        min_area = min(min_area, abs((x2 - x1) * (y2 - y1)))
        return min_area if min_area != float('inf') else 0

