from scipy.misc import comb


def Comb(c, n, k):
    if c[n][k]:
        return c[n][k]
    c[n][k] = comb(n, k)
    return c[n][k]


def P(C_vect, p, n, s):
    return sum(((-1) ** k * Comb(C_vect, n, k) * Comb(C_vect, p - s * k - 1, n - 1) for k in range((p - n) // s + 1))) / s ** n


def roll_dice(rolls, sides, threshold):
    if threshold > sides * rolls:
        return 0
    if threshold == sides ** rolls:
        return 1 / sides ** rolls
    if threshold <= rolls:
        return 1
    k_max = max((threshold - rolls) // sides, rolls - 1)
    n_max = max(sides, threshold - 1)
    C_vect = [[0 for _ in range(k_max + 1)] for _ in range(n_max + 1)]
    inv_prob = 0
    for t in range(rolls, threshold):
        inv_prob += P(C_vect, t, rolls, sides)
    return 1 - inv_prob
