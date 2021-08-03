class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        key = list(S.replace('-', '').upper())
        offset = len(key) % K
        if offset == 0:
            offset = K
        new_key = []
        i = 0
        while i < len(key):
            if i == 0:
                new_key.extend(key[:offset])
                i = offset
            else:
                new_key.append('-')
                new_key.extend(key[i:i + K])
                i = i + K
        return ''.join(new_key)
