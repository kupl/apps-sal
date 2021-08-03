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

        # 为了避免多次不必要的loop，只能用while loop！！！！！
        while i < int(num / i):
            if num % i == 0:
                result += i
                # / return float
                result += int(num / i)
            i += 1

        # 别忘了1 ！！！！
        return result + 1 == num
