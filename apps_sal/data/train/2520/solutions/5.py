class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = x < 0
        p = x
        if flag == True:
            p = -1 * x

        digit = []
        while p != 0:
            digit.append(p % 10)
            p = p // 10

        n = 0
        for i in digit:
            n = n * 10 + i

        if -2 ** 31 <= n <= 2 ** 31 - 1:
            return n if flag == False else -1 * n

        return 0
