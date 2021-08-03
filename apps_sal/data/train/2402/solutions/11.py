class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        buffer = ""
        s += " "
        while len(s) - 1 > 0:
            space_position = s.find(" ")
            buffer += s[space_position - 1::-1]
            buffer += " "
            s = s[space_position + 1:len(s)]
        buffer = buffer[:len(buffer) - 1]
        return buffer
