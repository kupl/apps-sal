class Solution:
     def maxSubArray(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         # i = 0
         # i_keep = 0
         # j = 1
         # j_keep = 1
         # max_sum = nums[0]-1
         # while j < len(nums) and i < j:
         #     temp_sum = sum(nums[i:j])
         #     if temp_sum >= max_sum:
         #         i_keep = i
         #         j_keep = j
         #         max_sum = temp_sum
         #     elif i == j-1:
         #         i += 1
         #         j += 1
         #     j += 1
         # return max_sum
         
         # brute force
         # max_sum = nums[0]
         # for i in range(len(nums)):
         #     for j in range(i,len(nums)+1):
         #         temp_sum = sum(nums[i:j])
         #         if temp_sum > max_sum and i != j:
         #             max_sum = temp_sum
         # return max_sum
 
         # outer loop only
         max_sum = csum = nums[0]
         for num in nums[1:]:
             if num >= csum + num:
                 csum = num
             else:
                 csum += num
             
             if csum > max_sum:
                 max_sum = csum
         
         return max_sum
                 
         

