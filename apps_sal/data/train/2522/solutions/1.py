class Solution:

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            (temp, pre, count) = ('', s[0], 0)
            for i in s:
                if i == pre:
                    count += 1
                else:
                    temp += str(count) + pre
                    count = 1
                    pre = i
            temp += str(count) + pre
            s = temp
        return s
