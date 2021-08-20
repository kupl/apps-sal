class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            if len(heap) < K:
                heapq.heappush(heap, [-(x * x + y * y), [x, y]])
            else:
                heapq.heappushpop(heap, [-(x * x + y * y), [x, y]])
        return [pair for (value, pair) in heap]
