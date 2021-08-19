class Solution:

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x
        (left, right) = (1, x)
        while 1:
            mid = left + (right - left) // 2
            if mid > x // mid:
                right = mid - 1
            else:
                if mid + 1 > x // (mid + 1):
                    return mid
                left = mid + 1
        return int(n)
