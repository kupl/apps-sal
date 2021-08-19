class Solution:

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        myset = set()
        result = 0
        if num == 1:
            return False
        i = 2
        while i < int(num / i):
            if num % i == 0:
                result += i
                result += int(num / i)
            i += 1
        return result + 1 == num
