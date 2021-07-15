class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        point_set = set([tuple(p) for p in points])
        
        min_area = float('inf')
        
        for idx, p1 in enumerate(points):
            for idx2 in range(idx, len(points)):
                p2 = points[idx2]
                
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    # search for other points
                    p3 = (p1[0], p2[1])
                    p4 = (p2[0], p1[1])
                    
                    if p3 in point_set and p4 in point_set:
                        # calc area
                        dx = abs(p1[0] - p2[0])
                        dy = abs(p1[1] - p2[1])
                        area = dx * dy
                        if area < min_area:
                            min_area = area
        return min_area if min_area != float('inf') else 0
                
            

