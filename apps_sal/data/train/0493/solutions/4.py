class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if sum(nums) < S:
            return 0
        if (S + sum(nums)) % 2 == 1:
            return 0
        target = (S + sum(nums)) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for n in nums:
            i = target
            while(i >= n):
                dp[i] = dp[i] + dp[i - n]
                i = i - 1
        return dp[target]
