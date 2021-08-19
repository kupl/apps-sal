class Solution:

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ['1']
        result = '1'
        for i in range(n - 1):
            start = 0
            temp = []
            while start < len(s):
                count = 1
                next = start + 1
                while next < len(s) and s[start] == s[next]:
                    next += 1
                    count += 1
                temp.append(str(count))
                temp.append(s[start])
                start = next
            result = ''.join(temp)
            s = temp
        return result
