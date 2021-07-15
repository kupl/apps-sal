class Solution:
     def singleNonDuplicate(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         while nums:
             if len(nums)>1 and nums[0]==nums[1] :
                 nums.pop(0)
                 nums.pop(0)
             else:
                 return nums[0]
             

