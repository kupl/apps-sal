class Solution:
     def longestCommonPrefix(self, strs):
         """
         :type strs: List[str]
         :rtype: str
         """
         if not strs:
             return ""
         
         s0 = strs[0]
         shortest_str_len = len(s0)
         
         for s in strs:
             shortest_str_len = min(shortest_str_len, len(s))
 
         for i in range(shortest_str_len):
             for s in strs:
                 if s[i] != s0[i]:
                     if i == 0:
                         return ""
                     else:
                         return s0[0:i]
        
         return s0[0:shortest_str_len]
