class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = - (x**2 + y**2)
            if len(heap) >= K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [[x, y] for dist, x, y in heap]
