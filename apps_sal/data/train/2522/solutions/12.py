class Solution:

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        n = n - 1
        string = '1'
        for i in range(n):
            a = string[0]
            count = 0
            final = ''
            for s in string:
                if a != s:
                    final += str(count)
                    final += a
                    count = 1
                    a = s
                else:
                    count += 1
            final += str(count)
            final += s
            string = final
        return final
