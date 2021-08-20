class Solution:

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum([n // 5 ** i for i in range(1, 20)])
