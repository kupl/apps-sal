class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # KMP
        i, j, m, n = -1, 0, len(haystack), len(needle)
        # construct jump array
        jump = [-1] * n
        while j < n - 1:  # j is increased by one
            if i == -1 or needle[i] == needle[j]:
                i, j = i + 1, j + 1
                jump[j] = jump[i] if needle[i] == needle[j] else i
            else:
                i = jump[i]

        # swipe
        i, j = 0, 0  # both start at 0
        while i < m and j < n:  # CAUTION j < n
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = jump[j]
        return i - j if j == n else -1
