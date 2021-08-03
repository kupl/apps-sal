class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = {}
        cnt, flag = 0, 0
        for i in s:
            c[i] = c.get(i, 0) + 1
        for i in c:
            cnt += (c[i] // 2) * 2
            if c[i] % 2 != 0:
                flag = 1
        return cnt + flag
