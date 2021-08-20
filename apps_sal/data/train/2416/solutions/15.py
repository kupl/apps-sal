class Solution:

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a = num
        while a * a > num:
            a = (a + num // a) // 2
        return a * a == num
