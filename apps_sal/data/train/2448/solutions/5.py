class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        base, extra, result = {}, 0, 0
        for letter in s:
            if letter in base:
                base[letter] += 1
            else:
                base[letter] = 1
        for value in base.values():
            if extra == 0 and value % 2 == 1:
                extra += 1
            result += value // 2 * 2
        return result + extra
