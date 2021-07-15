import heapq

class Distance:
    
    def __init__(self, p, d):
        self.d = d
        self.p = p
    
    def __lt__(self, other):

        return self.d >= other.d
        

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        
        def distance(p):
            return math.sqrt(p[0]**2+p[1]**2)
        
        distances_k = []
        for p in points:
            
            d = Distance(p, distance(p))
            
            if len(distances_k) < K:
                heapq.heappush(distances_k, d)
            elif d.d < distances_k[0].d:
                heapq.heappop(distances_k)
                heapq.heappush(distances_k, d)
                
        return [x.p for x in distances_k]
                
                
                
                
        
        
        
        
        
        

