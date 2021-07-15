class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
       
        pointsSet = set([(x, y) for x, y in points])
        minv = float('inf')
        for i in range(len(points)): 
            for j in range(i + 1, len(points)):
                if points[i][0] != points[j][0] and points[i][1] != points[j][1] and  (points[i][0], points[j][1]) in pointsSet and (points[j][0], points[i][1]) in pointsSet:
                    minv = min(minv, abs(points[i][0] - points[j][0])*abs(points[i][1] - points[j][1]))
                    if minv == 1: print((points[i], points[j]))
        return minv if minv != float('inf') else 0

