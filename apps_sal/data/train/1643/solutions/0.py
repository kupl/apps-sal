from scipy.special import comb


def almost_everywhere_zero(n, k):
    if k == 0:
        return 1
    (first, *rest) = str(n)
    l = len(rest)
    return 9 ** k * comb(l, k, exact=True) + (int(first) - 1) * 9 ** (k - 1) * comb(l, k - 1, exact=True) + almost_everywhere_zero(int(''.join(rest) or 0), k - 1)
