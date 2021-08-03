class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        up = x
        down = 0
        while True:
            n = (up + down) // 2
            if n**2 == x:
                return n
            elif n**2 < x:
                if (n + 1)**2 > x:
                    return n
                else:
                    down = n
            else:
                if (n - 1)**2 < x:
                    return n - 1
                else:
                    up = n
