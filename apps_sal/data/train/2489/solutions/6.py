class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr_min = float('inf')
        max_profit = 0

        for price in prices:
            curr_min = min(curr_min, price)
            profit = price - curr_min
            max_profit = max(max_profit, profit)

        return max_profit
