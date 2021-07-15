class Solution:
     def isHappy(self, n):
         """
         :type n: int
         :rtype: bool
         """
         former = set()
         while True:
             h = 0
             while n > 0:
                 d = n % 10
                 h += (d*d)
                 n = n // 10
             if h == 1:
                 return True
             elif h in former:
                 return False
             n = h
             former.add(n)
