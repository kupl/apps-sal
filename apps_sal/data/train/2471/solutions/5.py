class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        a = 1
        while a < n:
            dp[a + 1] = max(dp[a - 1] + nums[a], dp[a])
            a += 1
        return dp[n]
