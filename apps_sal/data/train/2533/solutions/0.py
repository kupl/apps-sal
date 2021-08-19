class Solution:

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((math.sqrt(8 * n + 1) - 1) / 2)
