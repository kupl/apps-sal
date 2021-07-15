class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hash_set = set(map(tuple, points))
        min_ = float('inf')

            
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    if (p1[0], p2[1]) in hash_set and (p2[0],p1[1]) in hash_set:
                        min_ = min(min_, abs(p2[0]-p1[0])*abs(p2[1]-p1[1]))
        
        if min_ == float('inf'):
            return 0
        
        return min_
