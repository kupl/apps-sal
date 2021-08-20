class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_before = prices[0]
        for i in prices:
            min_before = min(i, min_before)
            max_profit = max(max_profit, i - min_before)
        return max_profit
