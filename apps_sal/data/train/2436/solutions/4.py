class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = 0
        t = len(s) - 1
        while b < t:
            while b < t and not s[b].isalnum():
                b = b + 1
            while b < t and not s[t].isalnum():
                t = t - 1
            if s[b].lower() != s[t].lower():
                return False
            b = b + 1
            t = t - 1
        return True
