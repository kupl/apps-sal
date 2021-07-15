import numpy as np

N = 100001
xs = np.ones(N)
xs[:2] = 0
for i in range(2, N//2):
    xs[i*2::i] += 1


def count_pairs_int(diff, n_max):
    return sum(
        xs[i] == xs[i + diff]
        for i in range(1, n_max - diff)
    )
