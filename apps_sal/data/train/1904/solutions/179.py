class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            (x, y) = (point[0], point[1])
            dist = x ** 2 + y ** 2
            if len(max_heap) < K:
                heapq.heappush(max_heap, (-dist, x, y))
            elif dist < -max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-dist, x, y))
        return [[x, y] for (dist, x, y) in max_heap]
