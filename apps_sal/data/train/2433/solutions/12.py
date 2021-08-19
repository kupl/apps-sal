class Solution:

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if len(S) <= 1:
            return S.upper().strip('-')
        S = S.upper()
        n_dash = S.count('-')
        n = len(S) - n_dash
        form_S = ''
        if n % K == 0:
            begin_at = K - 1
        else:
            left = n % K
            begin_at = left - 1
        steps = 0
        abs_ind = 0
        norm_ind = 0
        while abs_ind <= begin_at and norm_ind < len(S):
            if S[norm_ind] == '-':
                norm_ind += 1
                continue
            form_S += S[norm_ind]
            abs_ind += 1
            norm_ind += 1
        form_S += '-'
        for char_ind in range(norm_ind, len(S)):
            if S[char_ind] == '-':
                continue
            elif steps == K - 1 and abs_ind > begin_at:
                form_S += S[char_ind] + '-'
                steps = 0
            else:
                form_S += S[char_ind]
                steps += 1
            abs_ind += 1
        return form_S.strip('-')
