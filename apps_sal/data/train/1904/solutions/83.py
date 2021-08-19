class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = [(float('-Inf'), 0, 0)] * K
        for (x, y) in points:
            heapq.heappushpop(heap, (-x ** 2 - y ** 2, x, y))
        res = []
        while heap:
            (val, row, col) = heapq.heappop(heap)
            res.append([row, col])
        return res
