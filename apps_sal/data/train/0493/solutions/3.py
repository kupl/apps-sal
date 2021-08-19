class Solution:

    def findTargetSumWays(self, nums, S):
        sum_ = sum(nums)
        if S > sum_:
            return 0
        target = sum_ - S
        if target % 2:
            return 0
        target = target // 2
        dp = [1] + [0] * target
        for n in nums:
            i = target
            while i >= n:
                dp[i] += dp[i - n]
                i -= 1
        return dp[target]
