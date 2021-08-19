class Solution:

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = s.split()
        if not v:
            return 0
        else:
            return len(v[-1])
