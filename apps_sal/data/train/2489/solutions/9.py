class Solution:
     def maxProfit(self, prices):
         max_profit = 0
         local_max = 0
         for i in range(1,len(prices)):
             if(local_max+prices[i]-prices[i-1]>0):
                 local_max += prices[i]-prices[i-1]
                 if(local_max>max_profit):
                     max_profit = local_max
             else:
                 local_max = 0
         return max_profit

