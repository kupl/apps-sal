class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        first = len(S) % K
        if first == 0:
            first = K
        blocks = [S[:first]]
        pos = first
        for k in range(len(S) // K):
            block = S[pos:pos + K]
            if len(block) > 0:
                blocks.append(block)
            pos += K
        return '-'.join(blocks)
