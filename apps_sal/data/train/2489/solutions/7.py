class Solution:

    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        (mincur, maxcur) = (prices[0], 0)
        for index in range(len(prices)):
            mincur = min(prices[index], mincur)
            maxcur = max(prices[index] - mincur, maxcur)
        return maxcur

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        (maxcur, maxpro) = (0, 0)
        for index in range(1, len(prices)):
            maxcur += prices[index] - prices[index - 1]
            maxcur = max(0, maxcur)
            maxpro = max(maxpro, maxcur)
        return maxpro
