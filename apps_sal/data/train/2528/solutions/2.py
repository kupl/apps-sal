class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        result = ''
        judge = strs[0]
        flag = True
        for i in range(len(judge)):
            for j in strs[1:]:
                if i >= len(j) or judge[i] != j[i]:
                    flag = False
            if flag:
                result += judge[i]
            else:
                break
        return result
