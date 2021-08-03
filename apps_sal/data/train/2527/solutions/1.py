class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        if b == 0:
            return a

        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF
        while b:
            carry = a & b
            a = (a ^ b) & mask
            b = carry << 1 & mask

        return a if a <= MAX else ~(a ^ mask)
