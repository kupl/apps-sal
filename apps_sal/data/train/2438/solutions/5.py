class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        spaces = 0
        word_started = False
        for i in range(1, len(s) + 1):
            if s[-i] == " " and word_started is False:
                spaces += 1
            elif s[-i] == " " and word_started is True:
                return i - 1 - spaces
            else:
                word_started = True
        if word_started is True:
            return len(s) - spaces
        else:
            return 0
