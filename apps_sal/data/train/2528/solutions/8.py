class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        cpy = strs.copy()
        return self.helper(cpy, 0)

    def helper(self, strs, i):
        if i == len(strs) - 1:
            return strs[i]
        s1 = strs[i]
        s2 = strs[i + 1]
        prefix = ""
        if len(s1) == 0 or len(s2) == 0:
            return prefix
        j = 0
        while j < len(s1) and j < len(s2) and s1[j] == s2[j]:
            j += 1
            prefix = s1[:j]
        i += 1
        strs[i] = prefix
        return self.helper(strs, i)
