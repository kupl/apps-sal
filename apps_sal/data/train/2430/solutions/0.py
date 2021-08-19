class Solution:

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 2 == 0:
            n = n >> 1
        cnt = 0
        a = n
        while a > 0:
            cnt += 1
            a = a >> 1
        if cnt % 2 == 0:
            return False
        c = 1
        for i in range(1, cnt):
            c = c << 1
            if i % 2 == 0:
                c += 1
        return c == n
