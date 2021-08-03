import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []

        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            if len(heap) < K:
                heapq.heappush(heap, (-dist, point))
                continue

            if -heap[0][0] > dist:
                heapq.heappush(heap, (-dist, point))
                heapq.heappop(heap)

        return [x[1] for x in heap]
