class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        ans = 0
        for i in range(len(prices) - 1, 0, -1):
            prices[i] -= prices[i - 1]
        for i in range(1, len(prices), 1):
            if prices[i] > 0:
                ans += prices[i]
        return ans
