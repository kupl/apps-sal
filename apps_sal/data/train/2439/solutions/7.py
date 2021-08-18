class Solution:
    def myNext(self, T):
        next = [-1]
        l = len(T)
        i, j = 0, -1
        while i < l:
            if j == -1 or T[i] == T[j]:
                i += 1
                j += 1
                next.append(int(j))
            else:
                j = next[j]
        return next

    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        arr = Solution().myNext(needle)
        l1 = len(haystack)
        l2 = len(needle)
        i, j = 0, 0
        while i < l1 and j < l2:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == l2:
                    return i - l2
            else:
                j = arr[j]
        return -1
