class Solution:

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if len(s) == 0 else ord(s[-1]) - ord('A') + 1 + 26 * self.titleToNumber(s[:len(s) - 1])
