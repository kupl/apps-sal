class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple, points))
        
        min_area = float('inf')
        
        for i, p1 in enumerate(points):
            for j in range(i):
                p2 = points[j]
                potential_area = abs(p1[0]-p2[0]) * abs(p1[1]-p2[1])
                
                if potential_area == 0 or potential_area > min_area:
                    continue
                    
                if (p1[0],p2[1]) in point_set and (p2[0],p1[1]) in point_set:
                    
                    min_area = min(potential_area, min_area)     
                    
        return 0 if min_area == float('inf') else min_area
