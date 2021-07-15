class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        minArea = float('inf')
        pointsSet = set()
        for x, y in points:
            pointsSet.add((x, y))
        
            
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2:
                    if (x1, y2) in pointsSet and (x2, y1) in pointsSet:
                        area = abs(x1-x2) * abs(y1-y2)
                        if area:
                            minArea = min(minArea, area)
                            
        return minArea if minArea != float('inf') else 0
