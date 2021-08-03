class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        max_value = 0x7FFFFFFF
        masking = 0xFFFFFFFF
        while b != 0:

            carry = a & b
            a = (a ^ b) & masking
            b = (carry << 1) & masking

        return a if a <= max_value else ~(a ^ masking)
