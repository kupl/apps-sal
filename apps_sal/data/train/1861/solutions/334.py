from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set(map(tuple, points))
        area = float(\"inf\")
        for i in range(len(points)):
            for j in range(i):
                p0, p1 = points[i], points[j]
                if p0[0] == p1[0] or p0[1] == p1[1]: continue
                if (p1[0], p0[1]) in S and (p0[0], p1[1]) in S:
                    area = min(area, abs((p1[1]-p0[1]) * (p1[0]-p0[0])))
        return area if area != float(\"inf\") else 0
            
