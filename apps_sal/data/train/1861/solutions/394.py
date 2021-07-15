import sys
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        minArea = sys.maxsize
        
        pointSet = set()
        for point in points:
            pointSet.add((point[0], point[1]))
        
        #print(pointSet)
        for i in range(0, len(points)):
            for j in range(i+1, len(points)):
                point1 = points[i]
                point2 = points[j]
                x1, y1 = point1[0], point1[1]
                x2, y2 = point2[0], point2[1]
                
                # same point
                if x1 == x2 or y1 == y2:
                    continue
                
                if (x1, y2) in pointSet and (x2, y1) in pointSet:
                    
                    area = abs(x2-x1) * abs(y2-y1)
                    minArea = min(minArea, area)
                    
        if minArea == sys.maxsize:
            return 0
        return minArea
