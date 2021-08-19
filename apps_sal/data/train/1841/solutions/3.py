class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        for num in arr:
            if len(heap) >= n // 2 + 1:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
        median = heap[0]
        heap = []
        for num in arr:
            if len(heap) >= k:
                heapq.heappushpop(heap, (abs(median - num), num))
            else:
                heapq.heappush(heap, (abs(median - num), num))
        return [num for (_, num) in heap]
