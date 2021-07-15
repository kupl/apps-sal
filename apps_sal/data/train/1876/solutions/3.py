class Solution:
     def reachNumber(self, target):
         """
         :type target: int
         :rtype: int
         """
         target=abs(target)
         
         n=math.ceil(((1+8*target)**0.5-1)/2)
         
         if target%2>0:
             if n%4==1 or n%4==2:
                 return n
             elif n%4==3:
                 return n+2
             else:
                 return n+1
         else:
             if n%4==3 or n%4==0:
                 return n
             elif n%4==1:
                 return n+2
             else:
                 return n+1

