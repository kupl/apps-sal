class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_ls = str.split()
        flag = True
        pattern_d, str_d = {}, {}
        if len(str_ls) != len(pattern):
            return False
        for i in range(len(pattern)):
            if (str_ls[i] in str_d) and (pattern[i] in pattern_d):
                if (str_d[str_ls[i]] != pattern[i]) or (pattern_d[pattern[i]] != str_ls[i]):
                    flag = False
            elif (pattern[i] not in pattern_d) and (str_ls[i] not in str_d):
                pattern_d[pattern[i]] = str_ls[i]
                str_d[str_ls[i]] = pattern[i]

            else:
                flag = False
        return flag
