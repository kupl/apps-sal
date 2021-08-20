class Solution:

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        nexts = [0] * len(needle)
        nexts[0] = -1
        if len(needle) > 1:
            nexts[1] = 0
        left = 0
        right = 2
        while right < len(needle):
            if needle[left] == needle[right - 1]:
                nexts[right] = left + 1
                left += 1
                right += 1
            elif nexts[left] > 0:
                left = nexts[left]
            else:
                nexts[right] = 0
                left = 0
                right += 1
        i = 0
        j = 0
        while i <= len(haystack) - len(needle):
            if j == len(needle):
                return i
            if haystack[i + j] == needle[j]:
                j += 1
            elif nexts[j] > 0:
                i = i + j - nexts[j]
                j = nexts[j]
            else:
                i = i + 1
                j = 0
        return -1
