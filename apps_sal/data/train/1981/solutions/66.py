class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        count = [0 for _ in range(n)]
        h = []
        requests.sort(key = lambda x: x[0])
        start = 0
        for s,e in requests:
            while h and h[0] < s:
                for i in range(start, h[0]+1):
                    count[i] += len(h)
                start = h[0]+1
                heapq.heappop(h)
            for i in range(start, s):
                count[i] += len(h)
            start = s
            heapq.heappush(h,e)
        while h:
            for i in range(start,h[0]+1):
                count[i] += len(h)
            start = h[0]+1
            heapq.heappop(h)  
        mod = 10**9+7
        return sum([c*v for c,v in zip(sorted(nums),sorted(count))])%mod
                
                    

