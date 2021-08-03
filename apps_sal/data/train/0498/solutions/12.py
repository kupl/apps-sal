class Solution:
    def rob(self, nums):
        def helper(nums):
            if not nums:
                return 0
            dp = [0] * (len(nums) + 1)
            dp[1] = nums[0]
            for i in range(2, len(nums) + 1):
                dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
            return dp[-1]

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # rob the last house or not, calculate the maximum
        return max(helper(nums[:len(nums) - 1]), nums[-1] + helper(nums[1:len(nums) - 2]))
