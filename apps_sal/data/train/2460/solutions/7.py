class Solution:
     def maxSubArray(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 0:
             return None
         
         result = nums[0]
         lastMax = nums[0]
     
         for i in range(1, len(nums)):
             lastMax = lastMax + nums[i] if lastMax + nums[i] >= nums[i] else nums[i]
             result = lastMax if lastMax > result else result
         
         return result

