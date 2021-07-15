class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        cnt = [0] * len(nums)
        requests = sorted(requests, key = lambda x: -x[0])
        q = []
        for idx in range(len(nums)):
            while requests and idx >= requests[-1][0]:
                s, e = requests.pop()
                heapq.heappush(q, (e, s))
            while q and idx > q[0][0]:
                heapq.heappop(q)
                
            cnt[idx] = len(q)
        
        cnt.sort()
        nums.sort()
        return sum(cnt[idx] * nums[idx] for idx in range(len(nums))) % (10**9 + 7)

