class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        requests = sorted(requests)
        repeated, dp, idx = [], [], 0
        for i in range(len(nums)):
            while dp and dp[0] < i:
                heapq.heappop(dp)
            while idx < len(requests) and requests[idx][0] <= i:
                heapq.heappush(dp, requests[idx][1])
                idx += 1
            repeated.append(len(dp))
        return sum([x * y for x, y in zip(sorted(nums), sorted(repeated))]) % (10**9 + 7)
