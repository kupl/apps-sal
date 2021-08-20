class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        s = -1 if x < 0 else 1
        v = int(str(abs(x))[::-1])
        if s == -1:
            t = -v & -2147483648
            if t == -2147483648:
                return -v
            else:
                return 0
        else:
            t = v & 2147483647
            if t == v:
                return v
            else:
                return 0
