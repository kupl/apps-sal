from collections import defaultdict

class Solution:
    
    def computeArea(self, point_a, point_b, point_c, point_d):
        width = abs(point_a[0] - point_b[0])
        height = abs(point_a[1] - point_d[1])
        return width*height
    
    def minAreaRect(self, points: List[List[int]]) -> int:
        \"\"\"
        A rectangle consists of four points:
        A ---- B
        |      |
        D ---- C
        
        Point B = [Cx, Ay]
        Point D = [Ax, Cy]

        \"\"\"

        point_set = set(map(tuple, points))
            
        minArea = None
        for i, point_a in enumerate(points):
            for point_c in points[i:]:

                # Make sure A and C have different x and y position
                # otherwise the rectangle will be of 0 width/height.
                if point_a[0] == point_c[0] or point_a[1] == point_c[1]:
                    continue

                point_b = (point_c[0], point_a[1])
                point_d = (point_a[0], point_c[1])
                
                if point_b in point_set and point_d in point_set:
                    area = self.computeArea(point_a, point_b, point_c, point_d)
                    if area > 0 and minArea is None or area < minArea:
                        minArea = area

        if minArea is None:
            return 0
        else:
            return minArea
