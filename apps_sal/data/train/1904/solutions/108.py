import heapq


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (-dist, point))
            if len(heap) > K:
                heapq.heappop(heap)
        return [tuple[1] for tuple in heap]
