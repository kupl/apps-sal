class Solution:

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_fives = 0
        while n > 0:
            n = n // 5
            n_fives += n
        return n_fives
