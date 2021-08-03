import heapq


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        if n == 0:
            return []
        arr.sort()
#    if n%2:
#      median = ( arr[n//2] )
#    else:
#      median = ( arr[n//2] + arr[n//2-1] ) / 2
        median = arr[(n - 1) // 2]
        heap = []  # min heap
        for num in arr:
            strength = abs(num - median)
            heapq.heappush(heap, (strength, num))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = [heap[i][1] for i in range(min(k, n))]
        return ans
    pass
