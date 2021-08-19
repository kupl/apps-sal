class Solution:

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 2147483647
        mask = 4294967295
        while b != 0:
            (a, b) = ((a ^ b) & mask, (a & b) << 1 & mask)
        return a if a <= MAX else ~(a ^ mask)
