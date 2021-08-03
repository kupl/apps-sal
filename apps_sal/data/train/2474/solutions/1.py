class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        low = 0
        high = x

        while low < high:
            mid = (high + low) / 2
            if abs(mid**2 - x) < 1e-6:
                return int(mid)
            elif mid**2 > x:
                high = mid
            else:
                low = mid
