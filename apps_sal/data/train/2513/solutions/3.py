class Solution:

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        digit = 0
        while True:
            temp = 9 * 10 ** digit
            if temp * (digit + 1) < n:
                n -= temp * (digit + 1)
                start += 10 ** digit * 9
                digit += 1
            else:
                break
        step = int(n / (digit + 1))
        start += step
        n -= (digit + 1) * step
        if n == 0:
            return start % 10
        start += 1
        return int(start / 10 ** (digit + 1 - n)) % 10
