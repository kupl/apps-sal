class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         n = len(prices)
         if n <=1:
             return 0
         else:
             minprice = prices[0]
             res = 0
             for i in range(1,n):
                 if prices[i] - minprice > res:
                     res = prices[i] - minprice
                 if prices[i]<minprice:
                     minprice = prices[i]
 
             return res
                     
             
         

