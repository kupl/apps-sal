class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        ## APPROACH : HEAP ##
        import heapq
        heap = []
        arr = sorted(arr)
        median = arr[( len(arr)-1 )//2]
        for i,num in enumerate(arr):
            heapq.heappush( heap, (abs(num - median), num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [ item[1] for item in heap ]
