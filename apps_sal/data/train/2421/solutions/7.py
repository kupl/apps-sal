class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         count = 0
         candidate = None
         
         for i in nums:
             if count == 0:
                 candidate = i
             count += (1 if i == candidate else -1)
         return candidate
