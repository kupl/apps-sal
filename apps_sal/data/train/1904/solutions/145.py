import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        sol = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1] **2)
            heapq.heappush(sol, (dist, point))
        print(sol)
        return [point[1] for point in heapq.nsmallest(K, sol)]
            

