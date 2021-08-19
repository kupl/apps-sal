class Solution:

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        hasOne = False
        while n > 0:
            if n & 1:
                if hasOne == True:
                    return False
                else:
                    hasOne = True
            n = n >> 1
        return hasOne
