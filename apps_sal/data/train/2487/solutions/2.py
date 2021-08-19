class Solution:

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        double_s = s + s
        return s in double_s[1:len(double_s) - 1]
