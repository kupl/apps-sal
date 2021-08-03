class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n < 0:
            n **= -1

        pow_ = True
        while n and pow_:
            if n == 1:
                return True
            pow_ = not(n % 2)
            n //= 2
        return pow_
