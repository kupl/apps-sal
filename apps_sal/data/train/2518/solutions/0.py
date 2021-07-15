class Solution:
     def checkPossibility(self, nums):
         """
         :type nums: List[int]
         :rtype: bool
         """
         possibility_flag = False
         for i in range(1, len(nums)):
             if nums[i] < nums[i-1]:
                 if possibility_flag:
                     return False
                 possibility_flag = True
                 if (i-2 < 0 or i-2 >= 0 and nums[i-2] < nums[i]) or (i+1 >= len(nums) or i+1 < len(nums) and nums[i+1] > nums[i-1]):
                     pass
                 else:
                     return False
         return True
 

