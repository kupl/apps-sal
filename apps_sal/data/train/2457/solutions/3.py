class Solution:
     def pivotIndex(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         left_sum = 0
         right_sum = sum(nums)
         for index in range(0, len(nums)):
             right_sum -= nums[index]
             if left_sum == right_sum:
                 return index
             left_sum += nums[index]
         return -1
     

