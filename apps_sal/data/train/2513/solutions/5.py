class Solution:

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        (i, count) = (1, 9)
        total = 9
        while total < n:
            i += 1
            count *= 10
            total += i * count
        n -= total - i * count + 1
        return int(str(n // i + 10 ** (i - 1))[n % i])
