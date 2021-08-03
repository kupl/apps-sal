class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        a = 0

        while n > 0:
            if a > 0:
                n = n // 26
            p = n % 26
            if p == 0:
                p = 26
            ans += chr(64 + p)
            n -= p
            a += 1

        return ans[::-1]
