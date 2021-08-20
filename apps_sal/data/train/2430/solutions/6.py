class Solution:

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = n % 2
        while n > 0:
            if i % 2 == 0:
                n /= 2
            else:
                n = (n - 1) / 2
            i += 1
        return n == 0
