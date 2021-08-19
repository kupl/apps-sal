class Solution:

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == '' and needle == '':
            return 0
        if needle == '':
            return 0
        if haystack == '' or needle == '' or len(haystack.split(needle)) == 1:
            return -1
        return len(haystack.split(needle)[0])
