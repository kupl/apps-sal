class Solution:
     def maxSubArray(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if len(nums) == 1:
             return nums[0]
         else:
             res = 0
             count = 0
             for i in range(len(nums)):
                 count += nums[i]
                 if count < 0:
                     count = 0
                 else:
                     res = max(res,count)
             if res == 0:
                 return max(nums)
             return res
