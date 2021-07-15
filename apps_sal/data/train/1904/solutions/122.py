class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def edistance(point):
            d=sqrt(point[0]**2 + point[1]**2)
            return d
        result=[]
        stk=[]
        for point in points:
            dis=edistance(point)
            heapq.heappush(stk,[dis,point])
        
        while K>0:
            result.append(heapq.heappop(stk)[1])
            K-=1
        return result

