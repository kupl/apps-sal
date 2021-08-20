class Solution:

    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            if n & 1:
                return False
            n >>= 1
        else:
            return True
