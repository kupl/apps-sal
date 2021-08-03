class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next(n):
            res = 0
            while n > 0:
                n, lsd = n // 10, n % 10
                res += lsd * lsd
            return res

        seen = set()
        while True:
            seen.add(n)
            n = next(n)
            if n == 1:
                return True
            if n in seen:
                return False
