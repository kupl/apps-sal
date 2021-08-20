class Solution:

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        i = 0
        res = []
        start = len(S) % K
        if start:
            res.append(S[:start])
            i = start
        while i < len(S):
            res.append(S[i:i + K])
            i += K
        return '-'.join(res)
