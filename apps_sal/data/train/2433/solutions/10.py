class Solution:

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(S.split('-'))
        S = S.upper()
        num_group = len(S) // K
        start_idx = len(S) % K
        ans = '' if start_idx == 0 else S[:start_idx]
        for i in range(num_group):
            end_idx = start_idx + K
            if start_idx > 0:
                ans += '-'
            ans += S[start_idx:end_idx]
            start_idx = end_idx
        return ans
