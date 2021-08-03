class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        factors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.append(i)
        for factor in factors:
            if num / factor not in factors and factor > 1:
                factors.append(num / factor)
        if num == sum(i for i in factors):
            return True
        else:
            return False
