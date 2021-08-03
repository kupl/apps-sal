class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, tail = 0, len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            ans += 1
            tail -= 1
        return ans
