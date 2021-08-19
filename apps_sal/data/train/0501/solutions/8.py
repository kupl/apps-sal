class Solution:

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        (length, i) = (len(s), 0)
        for j in range(length - 1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == length:
            return s
        remain = s[i:length + 1]
        rev_remain = remain[::-1]
        return rev_remain + self.shortestPalindrome(s[0:i]) + remain
