class Solution:

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '')
        l = len(S)
        res = l % K
        if res == 0:
            return '-'.join([S[i * K:(i + 1) * K].upper() for i in range(l // K)])
        else:
            lst = [S[0:res].upper()]
            return '-'.join(lst + [S[i * K + res:(i + 1) * K + res].upper() for i in range(l // K)])
