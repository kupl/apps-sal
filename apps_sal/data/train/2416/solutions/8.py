class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        p, r = 1, (num >> 1) + 1
        while p <= r:
            mid = (p + r) >> 1
            sq = mid * mid
            if sq == num:
                return True
            if sq >= num:
                r = mid - 1
            if sq <= num:
                p = mid + 1
        return False
