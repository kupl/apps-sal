class Solution:
     def addDigits(self, num):
         """
         :type num: int
         :rtype: int
         """
         return num if num < 10 else num%9 if num%9!=0 else 9
