class Solution:

    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 5:
            return False
        i = 2
        my_set = set({1})
        while i not in my_set and i < num // i:
            if num % i == 0:
                my_set.update([i, num // i])
            i += 1
        return sum(list(my_set)) == num
