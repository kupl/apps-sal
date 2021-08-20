from functools import reduce
from operator import xor
F = [[0] * 11 for i in range(10001)]
for x in range(1, 11):
    F[x][x] = y = 1
    for i in range(x + 1, 10001):
        y = y * i // (i - x)
        F[i][x] = F[i - 1][x] + y


def transform(A, x):
    return reduce(xor, (F[a][x] for a in A))
