from heapq import heappop,heappush,heapify
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        l1=[]
        l2=[]
        heapify(l1)
        for i in range(0,len(points)):
            heappush(l1, (-1*(points[i][0]*points[i][0] + points[i][1]*points[i][1]),i))
            if len(l1) > K:
                heappop(l1)
        while(len(l1) > 0):
            i = heappop(l1)
            l2.append(points[i[1]])
        return l2
                    
        

