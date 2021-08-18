class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        trz = 0
        div = 5
        while div <= n:
            trz += int(n / div)
            div *= 5
        return trz
