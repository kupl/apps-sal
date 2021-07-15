class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float(\"inf\")
        points_table = set((x,y) for x, y in points)
        
        for (x1, y1) in points:
            for (x2, y2) in points:
                if x1 > x2 and y1 > y2:
                    if (x1, y2) in points_table and (x2, y1) in points_table:
                        area = abs(x2-x1) * abs(y2-y1)
                        if area:
                            min_area = min(min_area, area)
        return min_area if min_area != float(\"inf\") else 0
                

        
        
        
