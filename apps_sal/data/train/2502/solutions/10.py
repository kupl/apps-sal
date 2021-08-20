class Solution:

    def maxProfit(self, prices):
        p = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                p += profit
        return p
