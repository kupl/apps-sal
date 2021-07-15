class Solution:
     def shortestPalindrome(self, s):
         """
         :type s: str
         :rtype: str
         """
         r=s[::-1]
         s=s+'#'+r
         lps=[0]*len(s)
 
         for i in range(1,len(s)):
             t=lps[i-1]
             if t>0 and s[i]!=s[t]:
                 t=lps[t-1]
             if s[i]==s[t]:
                 t+=1
             lps[i]=t
         return r[:len(r)-lps[-1]]+s[:len(r)]

