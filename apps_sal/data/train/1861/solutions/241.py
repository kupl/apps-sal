from collections import defaultdict
import math
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        d = dict()
        for x, y in points:
            if x not in d:
                d[x] = set()
            d[x].add(y)
            
        ans = float(\"inf\")
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if y2 in d[x1] and y1 in d[x2]:
                    ans = min(ans, abs((x2 - x1)) * abs((y2 - y1)))
        return 0 if ans == float(\"inf\") else ans
                    
                
                    
            
        
