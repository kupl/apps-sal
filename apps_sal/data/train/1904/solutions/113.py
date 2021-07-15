class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        pq = []
        
        def distance(point):
            return ( point[0]*point[0] + point[1]*point[1])
        for index, point in enumerate(points):
            heapq.heappush(pq,(distance(point),index,point))
            
        ans = []  
        k=0
        while pq and k<K:
            _,_,point = heapq.heappop(pq)
            ans.append(point)
            k+=1
        
        return ans

