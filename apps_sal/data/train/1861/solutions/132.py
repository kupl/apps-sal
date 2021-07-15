class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        for point in points:
            seen.add((point[0], point[1]))
        min_area = float('inf')
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2:
                    if (x1, y2) in seen and (x2, y1) in seen:
                        area = abs(y2 - y1) * abs(x2 - x1)
                        min_area = min(min_area, area)
        return 0 if min_area == float('inf') else min_area
