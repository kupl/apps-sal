import numpy as np


def two_by_n(n, k):
    x = np.array([[k * (k - 1), k * (k - 1)], [k, 0]])
    z = np.array([[k - 1, (k - 1) * (k - 2)], [k - 2, k ** 2 - 3 * k + 3]])
    for i in range(n - 2):
        x = np.array([np.diag(x @ z), x[0]]) % 12345787
    return sum(x[int(n == 1)]) % 12345787
