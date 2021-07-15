class Solution:
     def isHappy(self, n):
         """
         :type n: int
         :rtype: bool
         """
         
         count = {}
         
         while True:
             new_n = 0
             
             while n > 0:
                 new_n = new_n + (n % 10)**2
                 n = n // 10
             
             n = new_n
             
             if n == 1:
                 return True
             
             if n in count:
                 return False
             else:
                 count[n] = 1
