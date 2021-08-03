class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices), 1):
                if prices[i] >= prices[j]:
                    break
                else:
                    profit = max(profit, prices[j] - prices[i])
        return profit
