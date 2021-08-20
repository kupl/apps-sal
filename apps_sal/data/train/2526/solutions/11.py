class Solution:

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        elif n < 10:
            return 1
        i = 0
        while 5 ** (i + 1) <= n:
            i += 1
        s = n // 5
        j = 2
        while j <= i:
            s += n // 5 ** j
            j += 1
        return int(s)
