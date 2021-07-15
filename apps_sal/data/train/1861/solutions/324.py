class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = {(x, y) for x, y in points}
        n = len(points)
        result = float('inf')
        for i in range(1, n):
            for j in range(i):
                p1 = points[i]
                p2 = points[j]
                if p1[0] != p2[0] and p1[1] != p2[1] \\
                    and (p1[0], p2[1]) in point_set \\
                    and (p2[0], p1[1]) in point_set:
                    result = min( result, abs((p2[0]-p1[0]) * (p2[1]-p1[1])) )
        
        return result if result != float('inf') else 0
