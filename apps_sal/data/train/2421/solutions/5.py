class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         map = {}
         for n in nums:
             if n not in map:
                 map[n] = 0
             map[n] += 1
         max, occ = -1, -1
         for num, count in map.items():
             if count > occ:
                 max, occ = num, count
         return max
