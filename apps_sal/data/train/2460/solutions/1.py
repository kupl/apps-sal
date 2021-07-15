class Solution:
     def maxSubArray(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not nums:
             return None
         cur_sum = 0
         max_sum = nums[0]
         for n in nums:
             if cur_sum < 0:
                 cur_sum = n
             else:
                 cur_sum += n
             if cur_sum > max_sum:
                 max_sum = cur_sum
         return max_sum
