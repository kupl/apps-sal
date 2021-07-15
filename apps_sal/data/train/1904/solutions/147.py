import math

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) == 0:
            return []
        
        points.sort(key = lambda x: math.sqrt(x[0]*x[0] + x[1]*x[1]))
        
        return points[:K]

