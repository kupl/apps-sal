from itertools import accumulate
N_PALS = [0] + [9 * 10 ** ((n - 1) // 2) for n in range(1, 2001)]
S_PALS = list(accumulate(N_PALS))


def count_pal(n):
    return [N_PALS[n], S_PALS[n]]
