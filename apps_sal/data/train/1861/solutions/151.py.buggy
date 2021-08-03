class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float(\"inf\")
        points_table = set()
        for p in points:
            points_table.add(tuple(p))
        
        for x1, y1 in points:
            for x2, y2 in points:
                if x2 > x1 and y2 > y1:
                    if (x1, y2) in points_table and (x2, y1) in points_table:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        if area:
                            min_area = min(min_area, area)
        return 0 if min_area == float(\"inf\") else min_area
