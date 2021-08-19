class Solution:

    def makeNext(self, s):
        k = -1
        i = 0
        next = [None for i in range(len(s))]
        next[0] = -1
        while i < len(s) - 1:
            while k >= 0 and s[i] != s[k]:
                k = next[k]
            i += 1
            k += 1
            if s[i] == s[k]:
                next[i] = next[k]
            else:
                next[i] = k
        return next

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        Next = self.makeNext(needle)
        length = len(needle)
        for i in range(len(haystack)):
            count = 0
            while haystack[i + count] == needle[count]:
                count += 1
                if count + i >= len(haystack) and count < length:
                    return -1
                    break
                if count >= length:
                    return i
                    break
        return -1
