from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        p_set = set(map(tuple, points))
        
        res = float('inf')
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]

                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in p_set and (p2[0], p1[1]) in p_set:
                    area = abs(p1[0]-p2[0]) * abs(p1[1]-p2[1])
                    res = min(area, res)

        return 0 if res == float('inf') else res

