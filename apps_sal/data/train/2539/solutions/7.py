class Solution:
     def missingNumber(self, nums):
         
         return (sum(range(len(nums)+1)) - sum(nums))
         """ 
         :type nums: List[int]
         :rtype: int
         """
