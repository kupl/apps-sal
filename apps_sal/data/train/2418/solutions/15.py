class Solution:
     def containsDuplicate(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         seen = dict()
         for num in nums:
             if str(num) in seen:
                 return True
             else:
                 seen[str(num)] = 1
         return False
             

