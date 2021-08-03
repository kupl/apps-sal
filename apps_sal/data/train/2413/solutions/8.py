class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        if n == 2:
            return 987
        for a in range(1, 9 * pow(10, n - 1)):
            hi = (pow(10, n)) - a
            lo = int(str(hi)[::-1])
            if pow(a, 2) - 4 * lo < 0:
                continue
            if pow((pow(a, 2) - 4 * lo), 0.5) == int(pow((pow(a, 2) - 4 * lo), 0.5)):
                return (lo + pow(10, n) * (pow(10, n) - a)) % 1337
