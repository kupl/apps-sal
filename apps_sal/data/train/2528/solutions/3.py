class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        i = 0
        next_pref = 1
        while i < len(strs):
            if strs[i].startswith(res):
                pass
            else:
                res = res[:-1]
                break
            i += 1
            if i == len(strs):
                if next_pref == -1:
                    break
                res = strs[0][:next_pref]
                i = 0
                next_pref += 1
                if next_pref > len(strs[0]):
                    next_pref = -1
        return res
