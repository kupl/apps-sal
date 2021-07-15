class Solution:
     def strStr(self, haystack, needle):
         """
         :type haystack: str
         :type needle: str
         :rtype: int
         """
         if len(haystack) < len(needle):
             return -1
         if needle == '':
             return 0
         
         for i in range(len(haystack)):
             if haystack[i] == needle[0]:
                 res = True
                 j = 1
                 try:
                     while (j < len(needle)):
                         if haystack[i+j] == needle[j]:
                             j += 1
                         else:
                             res = False
                             break
                     if res:
                         return i
                 except:
                     return -1
         return -1
