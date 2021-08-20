import heapq


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        arr = [(-1 * (p[0] ** 2 + p[1] ** 2), p) for p in points]
        heap = arr[:K]
        heapq.heapify(heap)
        for p in arr[K:]:
            heapq.heappushpop(heap, p)
        return [coord for (distance, coord) in heap]
