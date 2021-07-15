class Solution:
     def searchInsert(self, nums, target):
         """
         :type nums: List[int]
         :type target: int
         :rtype: int
         """
         if target in nums:
             return nums.index(target)
         else:
             index = 0
             target -= 1
             while target > 0:
                 if target in nums:
                     return nums.index(target)+1
                 else:
                     target -= 1
             return index
