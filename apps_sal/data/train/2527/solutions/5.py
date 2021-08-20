class Solution:

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 2147483647
        MASK = 4294967296
        while b:
            (a, b) = ((a ^ b) % MASK, ((a & b) << 1) % MASK)
        return a if a <= MAX_INT else ~(a & MAX_INT ^ MAX_INT)
