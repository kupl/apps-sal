def fun(k):
     n = 1 + 8*k
     s = math.floor(n**0.5)-1
     s = s//2
     return s
 class Solution:
     def reachNumber(self, target):
         """
         :type target: int
         :rtype: int
         """
         if target<0:
             target *= -1
         L = [[3,2,1,1],[1,1,3,2]] 
         k = fun(target)
         if k*(k+1)/2==target:
             ans = 0
         else:
             ans = L[target%2][k%4]
         #print(target,"->",k,k+ans)
         return k+ans
         
