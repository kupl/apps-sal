class Solution:
     def maxSubArray(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 0:
             return 0
         res = curr = nums[0]                           
         for i in range(1, len(nums)):
             curr = max((curr + nums[i], nums[i]))
             res = max((res, curr))
         return res

