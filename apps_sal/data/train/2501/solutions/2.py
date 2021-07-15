class Solution:
     def reverseStr(self, s, k):
         """
         :type s: str
         :type k: int
         :rtype: str
         """
         list_s = list(s)
         n = len(list_s)
         for i in range(0,n,2*k):
             if n-i>=k:
                 list_s[i:i+k] = reversed(list_s[i:i+k])
             elif n-i<k:
                 list_s[i:] = reversed(list_s[i:])
                 
         return ''.join(list_s)
