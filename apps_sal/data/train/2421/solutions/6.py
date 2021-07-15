class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         a = sorted(nums)
         return a[int(len(a)/2)]

