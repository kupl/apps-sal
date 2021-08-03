class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        output = ""

        for i, word in enumerate(words):
            output += word[::-1]
            if i != len(words) - 1:
                output += " "

        return output
