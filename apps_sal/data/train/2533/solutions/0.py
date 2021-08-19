class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # brute force:
        #m = i (i+1) / 2
        #i = 0
        # while True:
        #    row = i * (i+1) / 2
        #    if n - row < 0:
        #        return i - 1
        #    i += 1

        # 2m = i (i+1)
        # i**2 + i - 2m = 0
        # i = -1 + sqr(8m) / 2
        return int((math.sqrt(8 * n + 1) - 1) / 2)
