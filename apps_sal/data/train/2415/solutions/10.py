class Solution:
     def searchInsert(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         i = 0
         n = len(nums)
         
         if n == 0:
             return 0 if nums[0] >= target else 1
         else:
             if nums[n-1] < target:
                 return n
             else:           
                 while i < n:
                     if nums[i] >= target:
                         return i
                     else:
                         i += 1

