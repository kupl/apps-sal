class Solution:
     def convertToTitle(self, n):
         """
         :type n: int
         :rtype: str
         """
         return "" if n == 0 else self.convertToTitle(int((n-1)/26)) + chr((n-1)%26+ord('A'))
