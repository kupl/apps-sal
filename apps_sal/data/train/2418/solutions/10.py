class Solution:
     def containsDuplicate(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         n_map = {}
         for n in nums:
             if n in n_map:
                 n_map[n] += 1
             else:
                 n_map[n] = 1
         for n, count in n_map.items():
             if count != 1:
                 return True
         return False
