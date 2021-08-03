class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        res = max(dp)
        for i in range(2, len(dp)):
            for j in range(i - 1):
                dp[i] = max(dp[i], dp[j] + nums[i])
                res = max(res, dp[i])

        return res
