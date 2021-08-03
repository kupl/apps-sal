class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = list(''.join(S.split('-')))
        tmp = [''.join(s[:len(s) % K])] + [''.join(s[i:i + K]) for i in range(len(s) % K, len(s), K)]
        return '-'.join(filter(None, tmp)).upper()
