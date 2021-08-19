class Solution:

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        s1 = len(S) % K if len(S) % K else K
        res = S[:s1]
        while s1 < len(S):
            res += '-' + S[s1:s1 + K]
            s1 += K
        return res
