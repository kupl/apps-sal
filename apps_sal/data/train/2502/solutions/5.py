class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        max1 = 0
        for i in range(1, len(prices)):
            print(max1)
            max1 += max(0, prices[i] - prices[i - 1])
        return max1
