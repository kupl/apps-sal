class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points or len(points) < 4:
            return 0
        
        pointsSet = set()
        
        minArea = float(\"inf\")
        for x1, y1 in points:
            for x2, y2 in pointsSet:
                if (x1,y2) in pointsSet and (x2, y1) in pointsSet:
                    minArea = min(minArea, self.getArea(x1,y1,x2,y2))
            pointsSet.add((x1, y1))
        
        return 0 if minArea == float(\"inf\") else minArea
                    
                
    
    def getArea(self, x1, y1, x2, y2) -> int:
        x = abs(x2 - x1)
        y = abs(y2 - y1)
        return x * y
