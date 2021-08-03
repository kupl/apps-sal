class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple, points)) 
        result = float(\"inf\")
        for k, p2 in enumerate(points):
            for i in range(k+1, len(points)):
                p1 = points[i]
                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in point_set and (p2[0], p1[1]) in point_set:
                    area = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                    result = min(result, area)
                    
        return result if result != float(\"inf\") else 0

