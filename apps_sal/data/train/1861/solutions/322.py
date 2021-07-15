from collections import defaultdict

class Solution:
    
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
        minArea = float('inf')

        for i, point_a in enumerate(points):
            for point_c in points[i:]:

                # Make sure A and C have different x and y position
                # otherwise the rectangle will be of 0 width/height.
                if point_a[0] == point_c[0] or point_a[1] == point_c[1]:
                    continue

                point_b = (point_c[0], point_a[1])
                point_d = (point_a[0], point_c[1])
                
                if point_b in point_set and point_d in point_set:
                    minArea = min(minArea,
                                  abs(point_a[0] - point_b[0])*abs(point_a[1] - point_d[1]))

        if minArea == float('inf'):
            return 0
        else:
            return minArea
