from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i in range(k):
            heappush(maxHeap, [-self.distance(points[i]), points[i]])
        for j in range(k, len(points)):
            if maxHeap[0][0] < -self.distance(points[j]):
                heappop(maxHeap)
                heappush(maxHeap, [-self.distance(points[j]), points[j]])
        return [points for (distance, points) in list(maxHeap)]
            
    def distance(self, coord):
        return coord[0]**2 + coord[1]**2
