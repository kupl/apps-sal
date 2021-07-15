class Solution:
     def hasAlternatingBits(self, n):
         """
         :type n: int
         :rtype: bool
         """
         bits = bin(n)
         return all(bits[i] != bits[i+1] for i in range(len(bin(n)) - 1) )
