class Solution:

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        hi = x // 2
        lo = 0
        if x == 1:
            return 1
        while True:
            if hi == lo:
                return hi
            if hi - lo == 1:
                if hi * hi > x:
                    return lo
                return hi
            test = (hi + lo) // 2
            sq = test * test
            if sq == x:
                return test
            if sq > x:
                hi = test - 1
            else:
                lo = test
