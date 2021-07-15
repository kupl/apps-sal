class Solution:
     def isPerfectSquare(self, num):
         sign = True
         i = 1
         while(sign):
             if(num == i * i):
                 return True
             elif(num > i * i):
                 i = i + 1
             else:
                 return False

