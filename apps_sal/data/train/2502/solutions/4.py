class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cum = 0
        for iprice in range(1, len(prices)):
            if prices[iprice - 1] < prices[iprice]:
                cum += prices[iprice] - prices[iprice - 1]
        return cum
