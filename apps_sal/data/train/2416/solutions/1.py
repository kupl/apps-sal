class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        yy = math.sqrt(num)
        ans_str = str(yy)
        ans = ans_str.split(".")
        if (int(ans[1]) == 0):
            return True
        else:
            return False
