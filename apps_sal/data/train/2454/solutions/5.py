class Solution:
     def convertToTitle(self, n):
         """
         :type n: int
         :rtype: str
         """
         
         if n <= 26:
             return chr(n + 64)
 
         out = ''
         r = n
         while r >= 1:
             out += chr((r-1) % 26 + 65)
             r = (r - 1) // 26
 
         return out[::-1]
