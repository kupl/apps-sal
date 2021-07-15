class Solution:
     def findTheDifference(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: str
         """
         S = [i for i in s]
         T = [i for i in t]
         for i in S:
             T.remove(i)
         return T[0]

