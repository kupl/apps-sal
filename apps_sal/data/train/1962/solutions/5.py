class Solution:
     def dominantIndex(self, nums):
 
         if len(nums) > 1:
             n = max(nums)
             id = nums.index(n)
             nums.remove(n)
             return id if n >= max(nums)*2 else -1
         else:
             return 0
