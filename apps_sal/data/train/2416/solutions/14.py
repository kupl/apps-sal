class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        i = 1
        while(True):
            if num / i < i:
                # print num / i
                return False
            else:
                if num / i == i:
                    return True
                else:
                    i += 1
