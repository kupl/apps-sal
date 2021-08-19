class Solution:

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x = str(x)[::-1]
            x = int(x) + 0
        else:
            x = str(-x)[::-1]
            x = 0 - int(x)
        if x < -2 ** 31 or x >= 2 ** 31 - 1:
            x = 0
        return x
        "\n         x = str(x)\n         if x[0] == '-':\n             x = x[1:]\n             ans = int()\n             "
