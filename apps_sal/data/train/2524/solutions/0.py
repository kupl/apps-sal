class Solution:
     def findLengthOfLCIS(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) < 1:
             return 0
         cur_len = 1
         max_len = 1
         for i in range(1,len(nums)):
             if nums[i] > nums[i-1]:
                 cur_len = cur_len + 1
             else:
                 cur_len = 1
                 
             if cur_len > max_len:
                 max_len = cur_len
         return max_len

