class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        pointsLookup = set(map(tuple, points))
        minArea = math.inf

        for i in range(0, len(points)-1):
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                # Find two potential diagonal points and see if other points of the rectangle
                # are present. If so, we've a rectangle.
                if p1[0] != p2[0] and p1[1] != p2[1] \\
                    and (p1[0], p2[1]) in pointsLookup and (p2[0], p1[1]) in pointsLookup:
                    area = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                    minArea = min(minArea, area)

        return minArea if minArea < math.inf else 0
