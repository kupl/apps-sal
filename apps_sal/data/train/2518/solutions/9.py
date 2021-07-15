class Solution:
     def checkPossibility(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         modified = False
         for i in range(1, len(nums)):
             if i and nums[i] < nums[i - 1]:
                 if modified:
                     return False
                 modified = True
                 if i > 1 and nums[i] <= nums[i - 2]:
                     nums[i] = nums[i - 1]
         return True
