import math

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = set(map(tuple, points))
        
        min_area = math.inf
        
        for start_x, start_y in points:
            for diag_x, diag_y in points:
                if diag_y < start_y and diag_x > start_x and (diag_x, start_y) in points and (start_x, diag_y) in points:
                    min_area = min(min_area, (diag_x - start_x) * (start_y - diag_y))
                    
        if min_area == math.inf:
            return 0
        else:
            return min_area
                    
        

