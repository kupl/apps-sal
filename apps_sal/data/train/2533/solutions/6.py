class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        upper = math.ceil(math.sqrt(2 * n))
        lower = math.floor(math.sqrt(2 * n)) - 2
        for k in range(lower + 1, upper):
            if (k + 1) * k <= 2 * n and (k + 2) * (k + 1) > 2 * n:
                return k
