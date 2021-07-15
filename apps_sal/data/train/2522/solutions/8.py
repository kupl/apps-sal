class Solution:
     def countAndSay(self, n):
         """
         :type n: int
         :rtype: str
         """
         res = '1'
         if n < 2:
             return res
         while 1:
             n -= 1
             if n == 0:
                 return res
             res = self._say(res)
 
     def _say(self, s):
         s += '*'
         curr, res = '', ''
         t = 0
         for i, c in enumerate(s):
             if i == 0:
                 curr = c
                 t = 1
             else:
                 if c == curr:
                     t += 1
                 else:
                     res = res + str(t) + curr
                     t = 1
                     curr = c
         return res
