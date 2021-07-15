class Solution:
     def findPairs(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: int
         """
         s = set(nums)
         total = 0
         if k < 0:
             return 0
         if k:
             for x in s:
                 if x + k in s:
                     total += 1
         else:
             counter = collections.Counter(nums)
             for k, v in counter.items():
                 if v > 1:
                     total += 1
         return total
