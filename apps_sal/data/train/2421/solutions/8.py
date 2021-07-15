class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not nums:
             return ""
         current = nums[0]
         counter = 1
         for i in range(1, len(nums)):
             if counter == 0:
                 current = nums[i]
                 counter = 1
             elif nums[i] == current:
                 counter += 1
             else:
                 counter -= 1
         return current
