class Solution:
     def longestCommonPrefix(self, strs):
         """
         :type strs: List[str]
         :rtype: str
         """
         if not strs or len(strs) == 0:
             return ""
         
         prefix = strs[0]
         
         if len(strs) > 1:
             for i, p in enumerate(prefix):
                 for j in range(1, len(strs)):
                     s = strs[j]
                     if i == len(s) or p != s[i]:
                         return prefix[:i]
                         
                     
                 
                 
             
         
         return prefix
                 
             
                     
         
         
         
             
             

