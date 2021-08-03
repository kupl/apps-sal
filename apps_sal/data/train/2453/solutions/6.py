class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {}
        while True:
            if str(n) in seen:
                return n == 1
            seen[str(n)] = True
            newN = 0
            while n > 0:
                n, mod = divmod(n, 10)
                newN += mod ** 2
            n = newN
        return False
