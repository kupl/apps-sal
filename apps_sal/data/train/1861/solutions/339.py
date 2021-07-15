class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        S = set(map(tuple, points))
        minArea = float('inf')
        
        for i, p1 in enumerate(points):
            for j in range(i):
                p2 = points[j]
                
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue
                
                if (p1[0], p2[1]) in S and \\
                   (p2[0], p1[1]) in S:
                    area = abs(p2[0] - p1[0]) * abs(p2[1] - p1[1])
                    minArea = min(minArea, area)
        
        if minArea == float('inf'):
            return 0
        return minArea
