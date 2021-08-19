class Solution:

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        ns = [1, 1]
        for i in range(2, n):
            ns[i % 2] = sum(ns)
        return sum(ns)
