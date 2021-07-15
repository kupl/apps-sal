class Solution:
     def trailingZeroes(self, n):
         """
         :type n: int
         :rtype: int
         """
         ans=0
         i=5
         while n//i:
             ans+=n//i
             i*=5
         return ans        
