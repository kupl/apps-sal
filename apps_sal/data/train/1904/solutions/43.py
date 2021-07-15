from queue import PriorityQueue
import math

class Solution:
    def kClosest(self, points, K):
        pq = PriorityQueue()
        
        for point in points:
            d = self.getDistance(point)
            pq.put((-1 * d, point))
            
            if pq.qsize() > K:
                pq.get()
                
        out = []
        while pq.qsize() > 0:
            out.append(pq.get()[1])
            
        return out
        
    def getDistance(self, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
