class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pointsSet = set()
        
        for x, y in points:
            pointsSet.add((x, y))
        
        minArea = float(\"inf\")
        for idx, point in enumerate(points):
            x1 = point[0]
            y1 = point[1]
            for x2, y2 in points[idx:]:
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in pointsSet and (x2, y1) in pointsSet:
                        curtArea = abs(x1 - x2) * abs(y1 - y2)
                        minArea = min(curtArea, minArea)
        if minArea == float(\"inf\"):
            return 0
        return minArea
            
