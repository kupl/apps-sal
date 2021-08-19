class Solution:

    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        for a in range(2, 9 * 10 ** (n - 1)):
            upper = 10 ** n - a
            lower = int(str(upper)[::-1])
            delta = a ** 2 - 4 * lower
            if delta >= 0 and int(delta ** 0.5) == delta ** 0.5 and ((a + delta) % 2 == 0):
                return (upper * 10 ** n + lower) % 1337
