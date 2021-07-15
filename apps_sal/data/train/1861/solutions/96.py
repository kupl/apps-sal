from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1,y2) in seen and (x2,y1) in seen:
                    # find the rectangle
                    res = min(res, abs(x1-x2)*abs(y1-y2))
            seen.add((x1,y1))
            
        return res if res < float('inf') else 0
                    
                

