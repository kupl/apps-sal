class Solution:
     def isPowerOfFour(self, num):
         return bin(num).count('1')==1 and bin(num).count('0')%2==1 and num>0
