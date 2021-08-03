class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_digit = 1
        while n > (n_digit * 9 * (10**(n_digit - 1))):
            n -= n_digit * 9 * (10**(n_digit - 1))
            n_digit += 1
        n_pre = (n - 1) // n_digit
        digit_position = (n - 1) % n_digit + 1
        num = 10**(n_digit - 1) + n_pre
        tmp = 0
        num = (num % 10**(n_digit - digit_position + 1)) // (10**(n_digit - digit_position))
        return num
