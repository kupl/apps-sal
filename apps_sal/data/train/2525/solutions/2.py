class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            count += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        return count
