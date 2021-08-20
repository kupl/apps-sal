class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        max_odd = 0
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        ans = 0
        single = 0
        for c in dic:
            if dic[c] % 2 == 0:
                ans += dic[c]
            else:
                ans += dic[c] - 1
                single = 1
        return ans + single
