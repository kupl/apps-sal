class Solution:

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x
        (left, right) = (0, x)
        mid = (right + left) / 2
        while abs(mid * mid - x) > 0.01:
            if mid > x / mid:
                right = mid
            else:
                left = mid
            mid = (right + left) / 2
        return int(mid)
