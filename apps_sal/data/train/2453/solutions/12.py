class Solution(object):
     def isHappy(self, n):
         aset = set()
         while n != 1 and n not in aset:
             aset.add(n)
             sums = 0
             while n:
                 digit = n % 10
                 sums += digit * digit
                 n = n // 10
             n = sums
         return n == 1
