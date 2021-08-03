class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prof = 0
        for j in range(len(prices) - 1):
            if prices[j + 1] > prices[j]:
                prof += prices[j + 1] - prices[j]
        return prof
