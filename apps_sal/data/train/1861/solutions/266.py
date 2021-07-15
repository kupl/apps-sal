class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        pointSet = set()
        
        for dx, dy in points:
            pointSet.add((dx, dy))
        minArea = float('inf')
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                if x1 != x2 and y1 != y2:
                    if (x2, y1) in  pointSet and (x1, y2) in pointSet:
                        
                        minArea = min(minArea,  abs(x2- x1) * abs(y2 - y1))

        
        return minArea if minArea < float('inf') else 0
                

