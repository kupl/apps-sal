class Solution(object):

    def largestPalindrome(self, n):
        if n == 1:
            return 9
        for a in range(2, 9 * 10 ** (n - 1)):
            hi = 10 ** n - a
            lo = int(str(hi)[::-1])
            if a ** 2 - 4 * lo < 0:
                continue
            if (a ** 2 - 4 * lo) ** 0.5 == int((a ** 2 - 4 * lo) ** 0.5):
                return (lo + 10 ** n * (10 ** n - a)) % 1337
