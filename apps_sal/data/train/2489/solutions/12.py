class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         if not prices: return 0
         min_val = prices[0]
         profit = 0
         for i in range(1, len(prices)):
             if profit < prices[i] - min_val:
                 profit = prices[i] - min_val
             if prices[i] < min_val:
                 min_val = prices[i]
 
         return profit
