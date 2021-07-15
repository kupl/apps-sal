class Solution:
     def dominantIndex(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         first=float('-Inf')
         second=float('-Inf')
         index=None
         for d,num in enumerate(nums):
             if num>first:
                 second=first
                 first=num
                 index=d
             if second<num<first:
                 second=num
         if second==0 or second==float('-Inf') or first/second>=2:
             return index
         else:
             return -1
