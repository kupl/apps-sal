import math


def points(n):
    if n == 0:
        return 1
    sum = 0
    for i in range(n):
        for j in range(1, n):
            if i * i + j * j <= n * n:
                sum += 1
    return 4 * sum + 5
