class Solution:
     def isAnagram(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: bool
         """
         memoS, memoT = {}, {}
         
         for c in s:
             if c not in memoS:
                 memoS[c] = 0
             memoS[c] += 1
         for c in t:
             if c not in memoT:
                 memoT[c] = 0
             memoT[c] += 1
             
         for v in memoS:
             if v not in memoT or memoT[v] != memoS[v]:
                 return False
         for v in memoT:
             if v not in memoS or memoS[v] != memoT[v]:
                 return False
         return True
