class Solution:
     def minMoves(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         n=len(nums)
         mn=min(nums)
 
         return sum(nums)-n*mn
