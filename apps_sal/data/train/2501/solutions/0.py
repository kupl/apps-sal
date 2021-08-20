class Solution:

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for idx in range(0, len(s), 2 * k):
            s = s[:idx] + s[idx:idx + k][::-1] + s[idx + k:]
        return s
