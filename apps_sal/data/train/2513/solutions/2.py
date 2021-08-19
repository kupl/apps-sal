class Solution:

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digitCount = 1
        totalNumbersWithDigitCount = 9 * 10 ** (digitCount - 1) * digitCount
        while n > totalNumbersWithDigitCount:
            n -= totalNumbersWithDigitCount
            digitCount += 1
            totalNumbersWithDigitCount = 9 * 10 ** (digitCount - 1) * digitCount
        baseNumber = 10 ** (digitCount - 1) - 1
        targetNumber = baseNumber + math.ceil(n / digitCount)
        targetDigitIndex = n % digitCount - 1
        return int(str(targetNumber)[targetDigitIndex])
