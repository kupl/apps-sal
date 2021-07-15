class Solution:
     def findLengthOfLCIS(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not len(nums):
             return 0
         res = 0
         temp_res = 1
         for i in range(len(nums)-1):
             if nums[i] < nums[i+1]:
                 temp_res += 1
             else:
                 if temp_res > res:
                     res = temp_res
                 temp_res = 1
         return max(res, temp_res)
