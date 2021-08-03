class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digs = 1
        while n > 9 * (10**(digs - 1)) * digs:
            n -= 9 * (10**(digs - 1)) * digs
            digs += 1
        return int(str(int(10**(digs - 1) + (n - 1) / digs))[n % digs - 1])
