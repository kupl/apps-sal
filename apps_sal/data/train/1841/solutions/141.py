from heapq import heappush, heappushpop


class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        nums = sorted([x for x in arr])
        median = nums[(n - 1) // 2]
        heap = []
        for i in range(n):
            if len(heap) < k:
                heappush(heap, (abs(arr[i] - median), arr[i]))
            elif abs(arr[i] - median) >= heap[0][0]:
                heappushpop(heap, (abs(arr[i] - median), arr[i]))
        return [x[1] for x in heap]
