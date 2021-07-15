from collections import defaultdict

class Solution:
    
    def minAreaRect(self, points: List[List[int]]) -> int:
        area = float('inf')
        gx = defaultdict(list)
        gy = defaultdict(list)
        
        for p in points:
            [x1, y1] = p
            
            if x1 in gx and y1 in gy:
                for y2 in gx[x1]:
                    if y2 in gy:
                        for x2 in gy[y2]:
                            if x2 in gy[y1]:
                                area = min(area, abs(x1-x2) * abs(y1-y2))
            gx[x1].append(y1)
            gy[y1].append(x1)
            
        return area if area < float('inf') else 0
                    
                    
                

