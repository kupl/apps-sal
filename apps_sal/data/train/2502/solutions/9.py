class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy = prices[0]
        sell = -1
        profit = 0
        i = 1
        while i < len(prices):
            if buy >= prices[i]:
                if sell > -1:
                    profit += sell - buy
                    sell = -1
                    buy = prices[i]
                else:
                    buy = prices[i]
            if prices[i] > buy:
                if prices[i] > sell:
                    sell = prices[i]
                else:
                    profit += sell - buy
                    sell = -1
                    buy = prices[i]

            i += 1
        if sell > -1:
            profit += sell - buy
        return profit
