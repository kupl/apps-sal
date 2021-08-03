class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def lcp(str1, str2):
            i = 0
            while (i < len(str1)) and (i < len(str2)):
                print((str1[i], str2[i]))
                if str1[i] == str2[i]:
                    i += 1
                else:
                    if i == 0:
                        return ""
                    else:
                        return str1[:i]
            if i == 0:
                return ""
            else:
                return str1[:i]
        if not strs:
            return ""
        if len(strs) == 1:
            if not strs[0]:
                return ""
            else:
                return strs[0]
        str = lcp(strs[0], strs[1])
        print(str)
        if len(strs) == 2:
            if not str:
                return ""
            else:
                return str
        for i in range(1, len(strs)):
            str = lcp(strs[i], str)
        if not str:
            return ""
        else:
            return str
