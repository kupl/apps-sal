from scipy.special import comb


def generate_diagonal(n, l):
    return [comb(n + a, a, exact=True) for a in range(l)]
