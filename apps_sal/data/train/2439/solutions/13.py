class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        next = self.next(needle)
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(needle):
            return i - j
        else:
            return -1

    def next(self, p):
        next = []
        next.append(-1)
        i = 0
        k = -1
        while i < len(p) - 1:
            if k == -1 or p[i] == p[k]:
                i += 1
                k += 1
                next.append(k)
            else:
                k = next[k]
        return next
