from math import pi


def iter_pi(epsilon):
    pi_4 = 0
    k = 0
    while abs(pi_4 * 4 - pi) > epsilon:
        pi_4 += (-1) ** k / (k * 2 + 1)
        k += 1
    return [k, round(pi_4 * 4, 10)]
