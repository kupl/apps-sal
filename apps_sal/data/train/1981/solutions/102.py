class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        
        ctr = collections.Counter()
        pq = []
        
        for s, e in requests:
            heapq.heappush(pq, (s, 1))
            heapq.heappush(pq, (e+1, -1))
        
        # print(pq)
        counts = 0
        for k in range(n):
            while pq and pq[0][0] == k:
                counts += heapq.heappop(pq)[1]
            ctr[k] = counts
        
        nums.sort()
        ans = 0
        for idx, ct in ctr.most_common():
            ans += nums.pop() * ct
        return ans % (10**9+7)

