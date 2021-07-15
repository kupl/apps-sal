class Solution:
     def missingNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         s = set()
         for num in nums:
             s.add(num)
         for i in range(len(nums) + 1):
             if i in s:
                 continue
             else:
                 return i
