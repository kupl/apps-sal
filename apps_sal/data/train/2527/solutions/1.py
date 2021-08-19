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
        MAX = 2147483647
        MIN = 2147483648
        mask = 4294967295
        while b:
            carry = a & b
            a = (a ^ b) & mask
            b = carry << 1 & mask
        return a if a <= MAX else ~(a ^ mask)
