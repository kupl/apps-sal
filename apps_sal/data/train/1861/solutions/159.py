class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        s = set(tuple(p) for p in points)
        
        area = math.inf
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i:]:
                if x1==x2 or y1==y2:
                    continue
                    
                if (x2, y1) not in s or (x1, y2) not in s:
                    continue
                    
                area = min(area, abs((x2-x1)*(y2-y1)))
                
        return area if area != math.inf else 0
