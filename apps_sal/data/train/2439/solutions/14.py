class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0

        if not haystack:
            return -1

        if len(haystack) < len(needle):
            return -1

        N = len(haystack)
        for i in range(N):
            if needle == haystack[i:i + len(needle)]:
                return i

        return -1
