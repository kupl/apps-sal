class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return True if n & (n - 1) == 0 and n != 0 else False
