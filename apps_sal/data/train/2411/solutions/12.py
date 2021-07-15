class Solution:
     def thirdMax(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         if not nums:
             return None
         nums = set(nums)
         if len(nums)<3:
             return max(nums)
         max3 = [-float('inf'),-float('inf'),-float('inf')]
         for n in nums:
             if n > max3[0]:
                 max3[0],max3[1],max3[2] = n,max3[0],max3[1]
             elif n > max3[1]:
                 max3[1],max3[2] = n, max3[1]
             elif n > max3[2]:
                 max3[2] = n
         return max3[2]

