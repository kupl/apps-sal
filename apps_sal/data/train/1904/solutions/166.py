class MyHeapObj():
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist
    
    def __gt__(self, other):
        return self.dist > other.dist

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pointsHeap = []
        for p in points:
            dist = (p[0]**2+p[1]**2)**0.5
            heapq.heappush(pointsHeap, MyHeapObj(p[0], p[1], dist))
            
        
        ret = []
        for i in range(K):
            point = heapq.heappop(pointsHeap)
            ret.append([point.x, point.y])
        return ret

