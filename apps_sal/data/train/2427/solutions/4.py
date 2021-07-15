class Solution:
     def findMaxConsecutiveOnes(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         ans=0
         c= 0
         for i in nums:
             c=i*c+i
             if c >ans:
                 ans = c
         return ans
