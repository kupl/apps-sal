def R(a, b):
    return range(a, b)


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
            D[i, k, L] = sum((F(i + 1, k - (j > 0), j == S[i]) for j in R(0, S[i] + 1)))
        else:
            D[i, k, L] = sum((F(i + 1, k - (j > 0), 0) for j in R(0, 10)))
        return D[i, k, L]
    return F(0, k, 0)
