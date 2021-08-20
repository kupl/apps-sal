class Solution:

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        w = []
        idx = 0
        while idx < len(s):
            w.append(s[idx:idx + k])
            idx += k
        w = [w[i][::-1] if i % 2 == 0 else w[i] for i in range(len(w))]
        return ''.join(w)
