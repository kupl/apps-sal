class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        return int(((2 * n) + 1.0 / 4)**0.5 - 0.5)
