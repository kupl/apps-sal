class Solution:
    import math

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        b = str(bin(n))
        b = b.replace('0b', '')
        b = b.replace('0', '')

        return len(b) == 1
