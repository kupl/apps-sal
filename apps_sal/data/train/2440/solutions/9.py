class Solution:

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}

        def f(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in list(cache.keys()):
                return cache[n]
            cache[n] = f(n - 1) + f(n - 2)
            return cache[n]
        return f(n)
