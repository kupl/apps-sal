class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        shortest = min(strs, key=len)
        for (i, val) in enumerate(shortest):
            for str in strs:
                if str[i] != val:
                    return shortest[:i]
        return shortest
