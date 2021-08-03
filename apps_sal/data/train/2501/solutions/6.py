class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for i in range(0, len(s), 2 * k):
            s1 = s[0:i]
            s2 = s[i:i + k][::-1]
            s3 = s[i + k:]
            s = s1 + s2 + s3
        return s
