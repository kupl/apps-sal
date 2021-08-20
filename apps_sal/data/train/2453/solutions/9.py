class Solution:

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sol = set()
        while n not in sol:
            sol.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1
