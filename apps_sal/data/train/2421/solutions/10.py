class Solution:
     def majorityElement(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         d = {}
         maxV = float('-inf')
         maxX = -1
         n = len(nums)//2
         for x in nums:
             if x not in d:
                 d[x] = 1
             else:
                 d[x] += 1
             if d[x] > maxV:
                 maxV = d[x]
                 maxX = x
             if maxV > n:
                 break                
         return maxX
