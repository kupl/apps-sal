class Solution:
     def containsDuplicate(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         xx = dict()
         for i in range(len(nums)):
             if nums[i] in xx:
                 return True
             else:
                 xx[nums[i]] = 1
         return False
