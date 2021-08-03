class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for i, p in enumerate(points):
            x, y = p
            dist = x**2 + y**2
            heapq.heappush(heap, (-dist, i))
            if len(heap) > K:
                heapq.heappop(heap)

        res = []
        for _, i in heap:
            res.append(points[i])

        return res
