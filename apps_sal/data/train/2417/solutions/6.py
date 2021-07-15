class Solution:
     def convertToBase7(self, num):
         """
         :type num: int
         :rtype: str
         """
         if num < 0:
             num *= -1
             r = '-'
         else:
             r = ''
         n = num
         c = 0
         while n // 7 > 0:
             c += 1
             n //= 7
         for i in range(c, 0, -1):
             t = num // (7 ** i)
             if t > 0:
                 num -= (7 ** i) * t
                 r += str(t)
             else:
                 r += '0'
         r += str(num)
         return r

