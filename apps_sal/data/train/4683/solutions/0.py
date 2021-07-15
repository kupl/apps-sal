from math import pi

def iter_pi(epsilon):
    n = 1
    approx = 4
    while abs(approx - pi) > epsilon:
        n += 1
        approx += (-4, 4)[n % 2] / (n * 2 - 1.0)
    return [n, round(approx, 10)]
