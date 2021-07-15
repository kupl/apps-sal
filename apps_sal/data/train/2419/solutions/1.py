class Solution:
     def repeatedStringMatch(self, A, B):
 
         times = 1
         tmp = A
         if (not set(B).issubset(set(A))):
             return -1
         maxTime = math.ceil(len(B) / len(A))
         while True:
             if B in A:
                 break
             elif (times <= maxTime):
                 A += tmp
                 times += 1
             else:
                 return -1
         return times
