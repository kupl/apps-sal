class Solution:
     def reverseStr(self, s, k):
         """
         :type s: str
         :type k: int
         :rtype: str
         """
         
         i = 0
         tmp = 0
         ret = ""
         while i < len(s):
             if len(s)-i < k:
                 tmp = len(s)-i
             else:
                 tmp = k
             ttmp = tmp    
             while ttmp!= 0:
                 ret += s[i+ttmp-1]
                 ttmp -= 1
             
             i+=tmp
             if len(s)-i < k:
                 tmp = len(s)-i
             else:
                 tmp = k
             ttmp = tmp
             
             while ttmp!= 0:
                 ret += s[i]
                 i+=1
                 ttmp -= 1
 
         return ret
