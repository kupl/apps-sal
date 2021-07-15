
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        point_set = set([tuple(x) for x in points])
            
        min_size = float('inf')
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    size = (y2-y1)*(x2-x1)
                    min_size = min(min_size, abs(size))
                    continue
                    
        if min_size == float('inf'):
            return 0
        return min_size
                

