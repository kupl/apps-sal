class Solution:
     def minMoves(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         min_num = min(nums)
         result = 0
         for num in nums:
             result += num-min_num
         return result
