class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        target = S + sum(nums)
        if target % 2 == 1 or sum(nums) < S:
            return 0
        target //= 2
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for curNum in nums:
            for cap in range(len(dp) - 1, -1, -1):
                if cap >= curNum:
                    dp[cap] += dp[cap - curNum]
        return dp[-1]
