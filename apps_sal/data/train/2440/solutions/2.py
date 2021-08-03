class Solution:
    def climbStairs(self, n):
        T = [1, 1]
        for i in range(2, n + 1):
            T[i % 2] = T[(i - 2) % 2] + T[(i - 1) % 2]
        return T[n % 2]

    def iterative_climbStairs(self, n):
        T = [-1] * n
        T[0] = 0
        T[1] = 1
        for i in range(2, n + 1):
            T[i] = T[i - 2] + T[i - 1]
        return T[n]

    def recursive_climbStairs(self, T, n):
        """
        :type n: int
        :rtype: int
        """
        if (n in T):
            return T[n]
        if (n < 0):
            return 0
        if (n < 2):
            return 1
        T[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        return T[n]
