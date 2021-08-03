import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []

        for p in points:
            dist = -(p[0] * p[0] + p[1] * p[1])
            heapq.heappush(heap, (dist, p[0], p[1]))

            if len(heap) > K:
                heapq.heappop(heap)

        res = [[p[1], p[2]] for p in heap]
        return res
