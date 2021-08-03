from math import pi


def iter_pi(epsilon):
    my_pi = 0
    n = sign = 1

    while epsilon < abs(pi - my_pi):
        my_pi += 4.0 / n * sign
        n += 2
        sign *= -1

    return [n // 2, round(my_pi, 10)]
