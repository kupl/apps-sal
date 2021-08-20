class Solution:

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lst = []
        if num < 1:
            return False
        if num == 1:
            return True
        i = 2
        while i < num + 1:
            print(num, i, ' ', lst)
            if num % i == 0:
                if i not in [2, 3, 5]:
                    lst.append(i)
                    if lst != []:
                        return False
                num = num // i
            else:
                i += 1
                if i > 5:
                    return False
        if lst == []:
            return True
