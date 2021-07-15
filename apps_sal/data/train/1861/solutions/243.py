class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        pointset = set([(x,y) for x,y in points])
        minArea = math.inf
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 != x2 and y1!=y2 and (x1, y2) in pointset and (x2, y1) in pointset:
                    area = abs((x1-x2)*(y1-y2))
                    minArea = min(area, minArea)
        
        return minArea if minArea < math.inf else 0
        
        
        # x     x    x
        #    x       x
        # x     x
#         x          x

