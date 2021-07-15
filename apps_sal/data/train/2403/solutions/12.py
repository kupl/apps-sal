class Solution:
     def checkPerfectNumber(self, num):
         """
         :type num: int
         :rtype: bool
         """
         
         if(num==1):
             return False
 
         sum=1
         i=2
         while i*i<=num:
             if(num%i==0):
                 sum+=i+num/i
             if(num/i==i):
                 sum-=i
          
             i+=1
         return sum==num

