from math import sqrt


def is_sqrt(x):
    y = sqrt(x)
    return y == round(y)


def closest_pair_tonum(x):
    for i in range(x - 1, 1, -1):
        for j in range(i - 1, 0, -1):
            if is_sqrt(i + j) and is_sqrt(i - j):
                return(i, j)
