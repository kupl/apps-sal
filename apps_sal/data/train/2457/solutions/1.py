class Solution:
     def pivotIndex(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if(len(nums) == 0 ):
             return -1
         leftSum = sum(nums) 
         rightSum = 0 
 
         for i in range(len(nums)):
             leftSum = leftSum - nums[i]
             if(rightSum == leftSum):
                 return i
             rightSum = rightSum + nums[i]
             
         return -1
