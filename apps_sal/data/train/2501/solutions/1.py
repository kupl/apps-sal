class Solution:
     def reverseStr(self, s, k):
         res = ''
         i = 0
         while i < len(s):
             if i + k <= len(s) and i + 2 * k > len(s) or i + k > len(s):
                 sub = s[i:i + k]
                 res += sub[::-1]
                 if i + 2 * k > len(s):
                     res += s[i + k:]
                 i = len(s)
             else:
                 sub = s[i:i + k]
                 res += sub[::-1]
                 res += s[i + k:i + 2 * k]
                 i += 2 * k
         return res

