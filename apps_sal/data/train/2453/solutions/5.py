class Solution:

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = {}
        add = 0
        while add != 1:
            add = 0
            for s in str(n):
                add += int(s) ** 2
            n = add
            if add in list(record.keys()):
                return False
            else:
                record[add] = 1
        return True
