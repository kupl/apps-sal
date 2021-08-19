class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        cpy = strs.copy()
        return self.__helper(cpy)
    '算出前面两个str的longest common prefix. 然后，把lcp放到第二个str的位置上，strs的第一个元素抛弃，\n     递归调用,直到最后只剩一个元素'

    def __helper(self, strs):
        if len(strs) == 1:
            return strs[0]
        s1 = strs[0]
        s2 = strs[1]
        prefix = ''
        if len(s1) == 0 or len(s2) == 0:
            return prefix
        j = 0
        while j < len(s1) and j < len(s2) and (s1[j] == s2[j]):
            j += 1
            prefix = s1[:j]
        strs[1] = prefix
        strs.pop(0)
        return self.__helper(strs)
