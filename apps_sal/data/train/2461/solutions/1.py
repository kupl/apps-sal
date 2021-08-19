class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # so let's take a look at what it means to be a power of two
        # 2^2 = 4 = 0100   | Now note when we subtract one | 2^2 - 1 = 3 = 0011
        # 2^3 = 8 = 1000   | Now note when we subtract one | 2^3 - 1 = 7 = 0111
        # Now note if we do n AND n-1, we should always get 0 | 1000 & 0111 = 0000 = 0
        return n > 0 and not (n & n - 1)
        # This holds true for all powers of 2. However note if we used 0 & anything else, it would show to be a power of 2.
        # To fix this we can add another clause v & (earlier clause) or we can simply check if value is greater than 0.
