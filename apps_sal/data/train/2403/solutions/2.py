class Solution:

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        ssum = 1
        i = 2
        while i ** 2 < num:
            if not num % i:
                ssum += i
                ssum += num / i
            i += 1
        return ssum == num
