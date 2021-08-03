class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, n = 0, len(s)

        for j in range(n - 1, -1, -1):
            if s[i] == s[j]:
                i += 1

        if i == n:
            return s

        return s[i:n][::-1] + self.shortestPalindrome(s[:i]) + s[i:]
