class Solution:
     def minMoves(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         # Adding n-1 elements by 1, same as subtracting one element by 1
         m = min(nums)
         res = 0
         for i in nums:
             res += (i - m)
         return res

