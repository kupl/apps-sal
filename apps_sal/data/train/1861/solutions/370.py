class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        
        hashset = set()
        
        for x, y in points:
            hashset.add((x, y))
        
        area = float('inf')
        for i in range(len(points)):
            for j in range(len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 >= x2 or y1 >= y2:
                    continue
                
                if (x1, y2) in hashset and (x2, y1) in hashset:
                    area = min(area, (y2-y1)*(x2-x1))
                
        return area if area < float('inf') else 0
