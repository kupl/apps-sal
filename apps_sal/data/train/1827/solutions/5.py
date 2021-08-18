class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)
        thisLen = int(math.log(num, 2)) + 1
        while thisLen > 2:
            thisBase = int(num ** (1.0 / (thisLen - 1)))
            if num * (thisBase - 1) == thisBase ** thisLen - 1:
                return str(thisBase)
            thisLen -= 1
        return str(num - 1)
