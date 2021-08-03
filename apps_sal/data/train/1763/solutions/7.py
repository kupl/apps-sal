from scipy.special import comb

MOD = 12345787


def insane_inc_or_dec(n):
    n %= MOD
    return (comb(n + 10, 10, exact=1) + comb(n + 9, 9, exact=1) - 10 * n - 2) % MOD
