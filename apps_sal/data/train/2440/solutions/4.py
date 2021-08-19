class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(i) = f(i-1) + f(i-2)
        if n == 0 or n == 1:
            return 1
        f2, f1 = 1, 1
        for i in range(2, n + 1):
            f = f1 + f2
            f2, f1 = f1, f
        return f

    def climbStairs(self, n):
        F = {0: 1, 1: 1}

        def f(i):
            if i in F:
                return F[i]
            else:
                F[i] = f(i - 1) + f(i - 2)
                return F[i]
        return f(n)
