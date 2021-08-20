class Solution:

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = num
        if n < 1:
            return False
        elif n == 1:
            return True
        else:
            while n >= 1:
                ncount = 0
                if n % 3 == 0:
                    n = n // 3
                    ncount = 1
                if n % 2 == 0:
                    n //= 2
                    ncount = 1
                if n % 5 == 0:
                    n //= 5
                    ncount = 1
                if ncount == 1:
                    pass
                else:
                    break
            if n == 1:
                return True
            else:
                return False
