class Solution:

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(((8 * n + 1) ** 0.5 - 1) / 2)
