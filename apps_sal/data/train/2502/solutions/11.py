class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit = [0] * (len(prices) + 1)
        pro_minus_pri = profit[0] - prices[0]
        for i in range(2, len(prices) + 1):
            profit[i] = max(profit[i - 1], prices[i - 1] + pro_minus_pri)
            pro_minus_pri = max(profit[i - 1] - prices[i - 1], pro_minus_pri)
        return profit[len(prices)]
