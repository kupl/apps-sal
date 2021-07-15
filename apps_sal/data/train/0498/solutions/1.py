class Solution:
     def rob(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums)==1: return nums[0]
         last, now= 0, 0
         for i in nums[:-1]: last, now = now, max(last+i, now)
         ret=now
         last, now= 0, 0
         for i in nums[1:]: last, now = now, max(last+i, now)
         return max(ret, now)
