class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        add = (N + 1) * [0]
        ded = (N + 1) * [0]
        M = len(requests)
        for start, end in requests:
            add[end + 1] += 1
            ded[start] += 1
        dp = N * [0]
        z1 = 0
        z2 = 0
        for i in range(N):
            z1 += add[i]
            z2 += ded[i]
            dp[i] = z2 - z1
        nums.sort()
        dp.sort()
        return sum(nums[i] * dp[i] for i in range(N)) % (10**9 + 7)
