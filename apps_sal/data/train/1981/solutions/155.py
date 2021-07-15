class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        heap_start = []
        heap_end = []
        for r in requests:
            heapq.heappush(heap_start, r[0])
            heapq.heappush(heap_end, r[1])
        current = 0
        p = []
        for n in range(len(nums)):
            while heap_start and heap_start[0]<=n:
                current += 1
                heapq.heappop(heap_start)
            while heap_end and heap_end[0]<n:
                current -= 1
                heapq.heappop(heap_end)
            p.append(current)
        
        heap = []
        for i, e in enumerate(p):
            heapq.heappush(heap, -e)
        ret = 0
        heapn = []
        for n in nums:
            heapq.heappush(heapn, -n)
        
        while heapn:
            n = heapq.heappop(heapn)
            ret +=  n*heapq.heappop(heap)
        return ret % (10**9+7)
            
            

