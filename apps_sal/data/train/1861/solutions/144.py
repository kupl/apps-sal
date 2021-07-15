class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        #Parallel with x, y -> find all point on same x, and same y that can form parallel edge
        
        def calculateArea(x1,x2,y1,y2):
            return abs(y2-y1) * abs(x2-x1)
        if not points or len(points) < 4: return 0
        
        visited = set()
        area = float('inf')
        for x1,y1 in points:
            for x2,y2 in visited:
                if (x1,y2) in visited and (x2,y1) in visited:
                    area = min(area, calculateArea(x1,x2,y1,y2))
            
            visited.add((x1,y1))
        
        return area if area != float('inf') else 0
        #Skip those that have less than len 2 (cant form a line)
        
        #  (1,5)        (6,5)       (x1,y2)         (x2,y2)
        #                       or 
        #  (1,2)        (6,2)       (x1,y1)         (x2,y1)

        # Rectangle would be
        

