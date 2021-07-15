class Solution:
     def productExceptSelf(self, nums):
         """
         :type nums: List[int]
         :rtype: List[int]
         """
         p = 1
         result = []
         for i in range(0, len(nums)):
             result.append(p)
             p = p * nums[i]
             
         p = 1
         
         for i in range(len(nums)-1, -1, -1):
             result[i] = result[i] * p
             p = p * nums[i]
         
         return result
