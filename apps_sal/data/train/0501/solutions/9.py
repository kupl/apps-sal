class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lps = [0, 1]
        x = 0
        for i in range(len(s) - 1, -1, -1):
            while x > 0 and s[i] != s[x]:
                x = lps[x - 1]
            if s[i] == s[x]:
                x += 1
            lps.append(x)
        print(lps)
        return s[:lps[~0] - 1:-1] + s
