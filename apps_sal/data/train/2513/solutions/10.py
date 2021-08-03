class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        g = 1
        while True:
            g_len = (10 ** g - 10 ** (g - 1)) * g
            if n <= g_len:
                break

            n -= g_len
            g += 1

        idx = (n - 1) // g
        pos = (n - 1) % g

        num = 10 ** (g - 1) + idx
        return int(str(num)[pos])
