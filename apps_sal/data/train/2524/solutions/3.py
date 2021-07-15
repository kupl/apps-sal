class Solution:
     def findLengthOfLCIS(self, nums):
         if nums == []:
             return 0
         elif len(nums) == 1:
             return 1
         ans, max_ans = 1, 1
         for i in range(len(nums) - 1):
             if nums[i] < nums[i + 1]:
                 ans += 1
                 max_ans = ans if ans > max_ans else max_ans
             else:
                 ans = 1
         return max_ans
         """
         :type nums: List[int]
         :rtype: int
         """

