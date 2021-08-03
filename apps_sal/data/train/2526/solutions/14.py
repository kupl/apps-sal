class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        num2 = 0
        div = 2
        quot = n // div
        while quot:
            num2 += quot
            div *= 2
            quot = n // div

        num5 = 0
        div = 5
        quot = n // div
        while quot:
            num5 += quot
            div *= 5
            quot = n // div

        return min(num2, num5)
