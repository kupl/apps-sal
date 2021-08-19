import sys
from fractions import gcd
import math


def euclid_algorithm(a, b):
    t1, t2 = abs(a), abs(b)
    # saving equalities:
    #t1 == x1 * a + y1 * b,
    # t2 == x2 * a + y2 * b.
    x1, y1, x2, y2 = int(math.copysign(1, a)), 0, 0, int(math.copysign(1, b))
    if t1 < t2:
        t1, t2 = t2, t1
        x1, y1, x2, y2 = x2, y2, x1, y1

    while t2 > 0:
        k = int(t1 // t2)
        t1, t2 = t2, t1 % t2
        #t1 - k * t2 == (x1 - k * x2) * a + (y1 - k * y2) * b
        x1, y1, x2, y2 = x2, y2, x1 - k * x2, y1 - k * y2

    return t1, x1, y1


def opposite_element(x, p):
    gcd, k, l = euclid_algorithm(x, p)
    if gcd != 1:
        return -1
    return k % p


n, m, k = [int(x) for x in input().split()]
g = gcd(n, m)
end = n * m // g
n1, m1 = n // g, m // g
l1 = opposite_element(n1, m1)


def solve(x, y):
    if x % (2 * g) != y % (2 * g):
        return float('inf')
    x1, y1 = x // (2 * g), y // (2 * g)
    t = x1 % n1 + n1 * ((y1 - x1 % n1) * l1 % m1)
    return x % (2 * g) + t * 2 * g


def check(x, y):
    res = min(solve(x, y), solve(-x, y), solve(x, -y), solve(-x, -y))
    return -1 if res >= end else res


for line in sys.stdin:
    x, y = [int(x) for x in line.split()]
    sys.stdout.write(str(check(x, y)) + '\n')
