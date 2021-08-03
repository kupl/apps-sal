class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor_result = x ^ y
        count = 0
        while xor_result > 0:
            count += xor_result & 1
            xor_result = xor_result >> 1

        return count
