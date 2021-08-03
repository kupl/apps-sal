class Solution:
    def getSum(self, a, b):
        max = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= max else ~(a ^ mask)
