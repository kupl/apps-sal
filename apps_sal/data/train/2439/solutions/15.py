class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        substr_len = len(needle)
        for index, char in enumerate(haystack):
            if haystack[index:index + substr_len] == needle:
                return index
        return -1
