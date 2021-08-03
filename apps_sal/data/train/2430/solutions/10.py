class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = None
        while n:
            curr = n % 2
            if curr == prev:
                return False
            prev = curr
            n //= 2

        return True
