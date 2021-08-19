class Solution:

    def getSum(self, a, b):
        max = 2147483647
        mask = 4294967295
        while b != 0:
            (a, b) = ((a ^ b) & mask, (a & b) << 1 & mask)
        return a if a <= max else ~(a ^ mask)
