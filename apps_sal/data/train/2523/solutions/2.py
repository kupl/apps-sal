class Solution:
     def findShortestSubArray(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         import collections
         c = collections.Counter(nums)
         degree = max(c[n] for n in c)
         if degree <=1:
             return degree
         res = {}
         for n in c:
             if c[n] == degree:
                 res[n] = [-1,-1]
         for i,n in enumerate(nums):
             if n in res:
                 if res[n][0] == -1 :
                     res[n][0] = i
                 else:
                     res[n][1] = i
         return min(res[i][1]-res[i][0] for i in res) + 1
