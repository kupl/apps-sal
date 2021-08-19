class Solution:

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if total < S or total + S & 1:
            return 0
        target = (S + total) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for n in nums:
            for i in range(target, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[target]
