class Solution:

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        now = n & 1
        while n:
            print(n, n & 1)
            n >>= 1
            if n & 1 == now:
                return False
            else:
                now = n & 1
        return True
