class Solution:
     def singleNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         count = 0
         for key in nums:
             count = count ^ key
         return count
 
         
             
                 
                 

