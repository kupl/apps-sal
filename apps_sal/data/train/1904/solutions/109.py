class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # given a list of x, y, return the smallest Kth  x^2 +y^2 pairs
        # need to maintain a Max heap of length K
        # BUT, Python does not support Max heap from heapq
        # We are going to x -1 to the distance and use a min heapp

        pq=[]
        for x, y in points:
            if len(pq)<K:
                heapq.heappush(pq, (-x*x-y*y,[x,y])) # (distance, [coordinate])
            else: 
                small_distance, small_coordinate = heapq.heappop(pq)
                if -x*x-y*y > small_distance:
                    heapq.heappush(pq, (-x*x-y*y,[x,y]))
                else:
                    heapq.heappush(pq, (small_distance,small_coordinate))

        
        return [_[1] for _ in pq]
