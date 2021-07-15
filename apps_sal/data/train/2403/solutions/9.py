class Solution:
     def checkPerfectNumber(self, num):
         """
         :type num: int
         :rtype: bool
         """
         if num <= 0: return False
         sum_of_divisors = 0
         n = 1
         while True:
             if n * n > num:
                 break
             if num % n == 0:
                 sum_of_divisors += n + num / n
             n += 1
         if (n-1)*(n-1) == num:
             sum_of_divisors -= n - 1
         return num == sum_of_divisors - num

