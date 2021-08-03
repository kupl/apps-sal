class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        mincur, maxcur = prices[0], 0
        for index in range(len(prices)):
            mincur = min(prices[index], mincur)
            maxcur = max(prices[index] - mincur, maxcur)
        return maxcur
