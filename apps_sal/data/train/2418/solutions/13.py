class Solution:
     def containsDuplicate(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         d = {}
         for num in nums:
             if num in d:
                 return True
             else:
                 d[num] = 1
         return False
         

