class Solution:
     def maximumProduct(self, nums):
         a = b = c = -1001
         d = e = 1001
         for num in nums:
             if num >= a:
                 c = b
                 b = a
                 a = num
             elif num >= b:
                 c = b
                 b = num
             elif num >= c:
                 c = num
                 
             if num <= d:
                 e = d
                 d = num
             elif num <= e:
                 e = num
         return max(a * b * c, a * d * e)

