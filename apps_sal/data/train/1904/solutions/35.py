from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if points is None:
            return []
        
        q = PriorityQueue()
        
        for point in points:
            q.put((-self.distanceOrigin(point), point))
            if q.qsize() > K:
                q.get()
                
        res = []
        while not q.empty():
            res.append(q.get()[1])
            
        return res

    
    def distanceOrigin(self, a):
        return sqrt(a[0]**2 + a[1]**2)
