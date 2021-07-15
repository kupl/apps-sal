class Solution:
     def helper(self, nums, cache = {}):
         if len(nums) == 0:
             return 0
         key = str(nums)
         if key in cache:
             return cache[key]
         cache[key] = max(nums[0] + self.helper(nums[2:]), self.helper(nums[1:]))
         return cache[key]
     def rob(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 0:
             return 0
         return max(nums[0] + self.helper(nums[2:-1]), nums[-1] + self.helper(nums[1:-2]), self.helper(nums[1:-1]))
