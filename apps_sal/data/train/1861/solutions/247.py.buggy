from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pts = set([(x,y) for x, y in points])
        min_area = float(\"inf\")
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2 and (x1, y2) in pts and (x2, y1) in pts:
                    min_area = min(abs(x1-x2)*abs(y1-y2), min_area)
        return min_area if min_area != float(\"inf\") else 0
                
            
        
