class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        index = K if len(S) % K == 0 and len(S) > 0 else len(S) % K
        result = S[:index]
        while index < len(S):
            result += '-' + S[index: index + K]
            index += K
        return result
