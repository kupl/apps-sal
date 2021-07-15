class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         # maximum profit at day i(assume i starts at 1)
         # doesn't sell: profit[i] = profit[i-1]
         # the index for prices subtract by 1
         # buy at day j, sell at day i: profit[i] = prices[i-1] + (profit[j-1]-prices[j-1])
         # if j=1: profit[i] = prices[i-1] + profit[0] - prices[0]
         # if j=(i-1): profit[i] = prices[i-1] + profit[i-2] - prices[i-2]
         # if i >= 2: profit[i] = max(profit[i-1], prices[i-1] + max(profit[j]-prices[j])(0<=j<=i-2))
         # if i == 1: profit[i] = profit[i-1]
         if len(prices) < 2: return 0
         profit = [0] * (len(prices) + 1)
         pro_minus_pri = profit[0] - prices[0]
         for i in range(2, len(prices) + 1):
             profit[i] = max(profit[i-1], prices[i-1] + pro_minus_pri)
             pro_minus_pri = max(profit[i-1] - prices[i-1], pro_minus_pri)
         return profit[len(prices)]

