class Solution:
     def missingNumber(self, nums):
         res = len(nums)
         for i in range(len(nums)):
             res = res ^ i
             res = res ^ nums[i]
         return res

