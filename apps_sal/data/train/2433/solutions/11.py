class Solution:
     def licenseKeyFormatting(self, S, K):
         """
         :type S: str
         :type K: int
         :rtype: str
         """
         
         s = list(S.upper())
         s = [c for c in s if c != '-']
         
         groups = []
         while s:
             group = s[-K:]
             groups.append(''.join(group))
             s[-K:] = []
             
         groups.reverse()
         return '-'.join(groups)

