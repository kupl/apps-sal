class Solution:
     def trailingZeroes(self, n):
         res = 5
         ans = 0
         while res < n+1:
             ans += int(n/res)
             res = 5*res
         return ans
