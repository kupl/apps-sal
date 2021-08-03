class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        \"\"\"
        :type points: List[List[int]]
        :type r: int
        :rtype: int
        \"\"\"
        res = 1
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                d = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
                if d > r * 2:
                   continue
                _x = (y2 - y1) * ((r * r - d * d/ 4.0) ** 0.5) / d
                _y = (x2 - x1) * ((r * r - d * d/ 4.0) ** 0.5) / d
                res = max(res, self.count(points, (x1 + x2) / 2.0 + _x, (y1 + y2) / 2.0 - _y, r))
                res = max(res, self.count(points, (x1 + x2) / 2.0 - _x, (y1 + y2) / 2.0 + _y, r))
        return res
        
    def count(self, points, x, y, r):
        count = 0
        for a, b in points:
            d = ((a - x)*(a - x) + (b - y)*(b - y))**0.5
            if d <= r + 0.0001 :
                count += 1
        return count
