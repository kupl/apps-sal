class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        rst = ""
        for i in range(len(s)):
            if (i // k) % 2:
                rst += s[i]
            else:
                rst += s[min(len(s), (i // k + 1) * k) - i % k - 1]
        return rst
