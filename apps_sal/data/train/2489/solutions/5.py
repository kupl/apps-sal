class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold = float('inf')
        result = 0
        for p in prices:
            if p > hold:
                result = max(result, p - hold)
            else:
                hold = p
        return result
