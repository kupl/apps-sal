from scipy.special import zeta, zetac


def doubles(maxk, maxn):
    return sum(((zetac(2 * k) - zeta(2 * k, 2 + maxn)) / k for k in range(1, maxk + 1)))
