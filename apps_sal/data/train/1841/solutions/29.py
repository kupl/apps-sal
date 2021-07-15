class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        import heapq
        n = len(arr)
        
        sort = sorted(arr)
        if n % 2 == 1:
            m = sort[n//2]
        else:
            m = sort[(n-1)//2]
        
        heap = []
        heapq.heapify(heap)
        for num in arr:
            val = abs(num-m)
            heapq.heappush(heap, (-val, -num))
        
        ret = []
        for i in range(k):
            val, num = heapq.heappop(heap)
            ret.append(-num)
        return ret

