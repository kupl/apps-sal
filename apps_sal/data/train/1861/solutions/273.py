from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # (1,1), (1,3), (3, 1), (3,3)
        # (1,1), (1,3), (3,1), (3,3) X (3,1), (3,3), (4,1), (4,3)
        
        point_set = set()
        for x, y in points:
            point_set.add((x, y))
            
        min_area = float('inf')
        for i, (x1, y1) in enumerate(points):
            for (x2, y2) in points[i+1:]:
                if x1 == x2 or y1 == y2:
                    continue

                if (x1, y2) in point_set and (x2, y1) in point_set:
                    min_area = min(min_area, abs((x1-x2) * (y1-y2)))
            
        return min_area if min_area != float('inf') else 0
            
        #x1, y1    x2, y1
        #x1, y2    x2, y2
        
        #3, 3      
        #3,4       4, 4

