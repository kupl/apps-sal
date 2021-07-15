class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        \"\"\"
        horizontal line if yi == yj
        veritcal line if xi == xj
        
        valid rectangle:
        - p1, p2, p3, p4 such that
        \"\"\"
        
        min_area = float('inf')
        
        pts = {(x,y) for x,y in points}
        
        for x1,y1 in pts:
            for x2,y2 in pts:
                if x2 > x1 and y2 > y1: #first pt is bottom left vertex, second pt is upper right vertex
                    if (x1, y2) in pts and (x2, y1) in pts:
                        min_area = min(min_area, abs(x2-x1) * abs(y2-y1))
                        
        if min_area == float('inf'):
            return 0
        return min_area
