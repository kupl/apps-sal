class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xys = set()
        for point in points:
            xys.add((point[0], point[1]))
            
        sq_min = float('inf')
        for i, pointi in enumerate(points):
            xi, yi = pointi[0], pointi[1]
            for j in range(i+1, len(points)):
                xj, yj = points[j][0], points[j][1]
                if xi != xj and yi != yj and (xi, yj) in xys and (xj, yi) in xys:
                    sq_min = min(sq_min, abs((xi-xj)*(yi-yj)))
        
        return sq_min if sq_min != float('inf') else 0
