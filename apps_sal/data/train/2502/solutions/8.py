class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        hold = -prices[0]
        sell = 0
        for i in range(1, len(prices)):
            sell = max(sell, hold + prices[i])
            hold = max(hold, sell - prices[i])
        return max(hold, sell)
