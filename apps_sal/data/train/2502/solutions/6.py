class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         profit = 0
         for i in range(0, len(prices)-1):
             if prices[i] < prices[i+1]:
                 profit = profit + prices[i+1] - prices[i]
         return profit
