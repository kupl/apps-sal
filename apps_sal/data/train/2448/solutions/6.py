class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for ss in s:
            dic[ss] = dic.get(ss, 0) + 1
        res = 0
        for (_, value) in list(dic.items()):
            res += value // 2 * 2
        if res < len(s):
            res += 1
        return res
