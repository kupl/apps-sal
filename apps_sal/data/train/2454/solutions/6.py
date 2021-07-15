class Solution:
     def convertToTitle(self, n):
         """
         :type n: int
         :rtype: str
         """
         letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
         result = ''
         while n:
             n -= 1
             result = letters[n % 26] + result
             n //= 26
         
         return result
