class Solution:
     def findLongestChain(self, pairs):
         """
         :type pairs: List[List[int]]
         :rtype: int
         """
         pairs = sorted(pairs,key=lambda x:x[1])
         res = 1
         first = pairs[0]
         for i in pairs[1:]:
             if first[-1] < i[0]:
                 res += 1
                 first = i
         return res

