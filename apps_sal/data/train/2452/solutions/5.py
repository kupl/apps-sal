class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1 and heap[0] != 0:
            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))
        return -heap[0]
