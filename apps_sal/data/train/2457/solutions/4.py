class Solution:
     def pivotIndex(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         n = sum(nums)
         sum_num = n
         for i in range(len(nums)):
             n-=nums[i]
             if (sum_num-nums[i])/2 == n:
                 return i
         return -1
