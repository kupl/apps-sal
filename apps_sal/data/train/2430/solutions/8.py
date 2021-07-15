class Solution:
     def hasAlternatingBits(self, n):
         """
         :type n: int
         :rtype: bool
         """
         bin1 = str(bin(n)[2:])
         length = len(bin1)
         for i in range(0,length-1):
             if bin1[i]==bin1[i+1]:
                 return False
         
         return True
         

