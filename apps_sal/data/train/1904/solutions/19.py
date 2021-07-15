class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        
        distance = [   ((x[0]**2 + x[1]**2)**(1/2),i) for i,x in enumerate(points)    ]
        heapq.heapify(distance)
        ans = []
        
        while K > 0 :
            element = heapq.heappop(distance)
            ans.append(points[element[1]])
            K -= 1
        return ans
