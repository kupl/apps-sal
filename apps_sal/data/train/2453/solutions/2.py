class Solution:

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo = set()
        while n != 1:
            n = sum([int(digit) ** 2 for digit in str(n)])
            if n in memo:
                return False
            memo.add(n)
        return True
