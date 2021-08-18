class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        pq = []
        for x, y in points:
            if len(pq) < K:
                heapq.heappush(pq, (-x * x - y * y, [x, y]))
            else:
                small_distance, small_coordinate = heapq.heappop(pq)
                if -x * x - y * y > small_distance:
                    heapq.heappush(pq, (-x * x - y * y, [x, y]))
                else:
                    heapq.heappush(pq, (small_distance, small_coordinate))

        return [_[1] for _ in pq]
