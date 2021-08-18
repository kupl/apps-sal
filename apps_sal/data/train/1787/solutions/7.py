from statistics import mean, pvariance
from copy import deepcopy


def matrix_transpose(m):
    return [list(i) for i in zip(*m)]


def matrix_matrix_multiply(a, b):
    n, p, m = len(a), len(b), len(b[0])
    c = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                c[i][j] += a[i][k] * b[k][j]

    return c


def matrix_vector_multiply(a, b):
    n, p = len(a), len(b)
    c = [0] * n

    for i in range(n):
        for k in range(p):
            c[i] += a[i][k] * b[k]

    return c


def matrix_solve(x, y):
    n, u, v = len(x), deepcopy(x), deepcopy(y)

    for i in range(n - 1):
        for j in range(i + 1, n):
            k = u[j][i] / u[i][i]
            u[j] = [a - k * b for a, b in zip(u[j], u[i])]
            v[j] = v[j] - k * v[i]

    for i in reversed(range(n)):
        v[i] = (v[i] - sum([v[j] * u[i][j] for j in range(i + 1, n)])) / u[i][i]

    return v


def features(x):
    return [1, x, x ** 2, x ** 3, x ** 4, x ** 5]


class Datamining:
    def __init__(self, train_set):
        x, y = zip(*train_set)

        design = [features(i) for i in x]
        t_design = matrix_transpose(design)

        cov = matrix_matrix_multiply(t_design, design)

        self.beta_hat = matrix_solve(cov, matrix_vector_multiply(t_design, y))

    def predict(self, x):
        z = features(x)

        return sum([a * b for a, b in zip(z, self.beta_hat)])
