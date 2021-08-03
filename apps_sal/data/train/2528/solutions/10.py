class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        cpy = strs.copy()
        return self.__helper(cpy)  # 记得加 self

    def __helper(self, strs):
        if len(strs) == 1:
            return strs[0]
        s1 = strs[0]
        s2 = strs[1]
        prefix = ""
        if len(s1) == 0 or len(s2) == 0:
            return prefix
        j = 0
        while j < len(s1) and j < len(s2) and s1[j] == s2[j]:
            j += 1
            prefix = s1[:j]
        strs[1] = prefix
        strs = strs[1:]
        return self.__helper(strs)  # 记得加 self
