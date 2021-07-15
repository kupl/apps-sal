class Solution:
     def rob(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not nums:
             return 0
         if len(nums)==1:
             return nums[0]
         return max(self.helper(nums[1:]), self.helper(nums[:-1]))
         
     def helper(self,nums):
         now = prev = 0
         for nxt in nums:
             now, prev = max(nxt+prev, now), now
         return now

