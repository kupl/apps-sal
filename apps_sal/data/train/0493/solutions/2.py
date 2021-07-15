class Solution:
     def findTargetSumWays(self, nums, S):
         """
         :type nums: List[int]
         :type S: int
         :rtype: int
         """
         def findTargetNumber(nums, target):
             print(nums, target)
             dp = [0 for _ in range(target + 1)]
             dp[0] = 1
             for n in nums:
                 for i in range(target, n - 1, -1):
                     dp[i] += dp[i - n]
             return dp[-1]
         
         sumResult = sum(nums)
         if (S + sumResult) % 2 != 0 or sumResult < S:
             return 0
         else:
             return findTargetNumber(nums, int((sumResult + S) / 2))
