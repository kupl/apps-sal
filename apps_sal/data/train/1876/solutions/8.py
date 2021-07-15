class Solution:
     def reachNumber(self, target):
         """
         :type target: int
         :rtype: int
         """
         target = abs(target)
         s = 0
         for i in range( target+1):
             s += i
             if s >= target:
                 break
         if (s - target)&1 :
             if (i+1)&1:
                 return i+1
             else:
                 return i+2
         else:
             return i
 
 

