import math

def iter_pi(epsilon):
    my_pi = i = 0
    while abs(my_pi - math.pi) > epsilon:
        my_pi += 4 * math.pow(-1, i) / (2 * i + 1)
        i += 1
    return [i, round(my_pi, 10)]
