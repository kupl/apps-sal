def almost_everywhere_zero(S, k):
    S = [int(c) for c in str(S)]
    (D, n) = ({}, len(S))

    def F(i, k, L):
        if i == n:
            return k == 0
        if k == 0:
            return F(i + 1, k, L)
        if (i, k, L) in D:
            return D[i, k, L]
        if i == 0 or L:
            D[i, k, L] = F(i + 1, k, S[i] == 0) + (S[i] - 1) * F(i + 1, k - 1, False) + F(i + 1, k - 1, S[i] != 0)
        else:
            D[i, k, L] = F(i + 1, k, False) + 9 * F(i + 1, k - 1, False)
        return D[i, k, L]
    return F(0, k, 0)
