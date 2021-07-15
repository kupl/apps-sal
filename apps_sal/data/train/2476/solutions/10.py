class Solution:
     def addDigits(self, num):
         """
         :type num: int
         :rtype: int
         """
         return 9 if num != 0 and num % 9 == 0 else num % 9
