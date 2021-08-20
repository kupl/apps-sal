class Solution:

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        root = 1
        while root * root < num:
            root = root + 1
        if root * root == num:
            return True
        return False
