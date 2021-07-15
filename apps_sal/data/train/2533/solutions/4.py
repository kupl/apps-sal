class Solution:
     def arrangeCoins(self, n):
         """
         :type n: int
         :rtype: int
         """
         # result = 0
         # if n < 2 :
         #     return n
         # for i in range(1,n+1):
         #     result += i
         #     if result > n:
         #         return i-1
         
         return  int(((2*n)+1.0/4)**0.5 - 0.5)
         
         
         
         
 #         left, right = 0, n
 #         while left <= right:
 #             mid = (left + right) // 2
 #             if self.totalCoins(mid) <= n < self.totalCoins(mid + 1) :
 #                 return mid
 #             elif n < self.totalCoins(mid):
 #                 right = mid
 #             else:
 #                 left = mid + 1
     
     
 #     def totalCoins(self, row):
 #         return (1 + row)*row //2

