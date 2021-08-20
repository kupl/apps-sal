from math import pi, pow


def iter_pi(epsilon):
    i = 0
    leibniz_i = 1
    while abs(4 * leibniz_i - pi) > epsilon:
        i += 1
        leibniz_i += pow(-1, i) * 1 / (2 * i + 1)
    return [i + 1, round(leibniz_i * 4, 10)]
