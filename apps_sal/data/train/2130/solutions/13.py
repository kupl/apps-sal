import math


def euclid_algorithm(a, b):
    (t1, t2) = (abs(a), abs(b))
    (x1, y1, x2, y2) = (int(math.copysign(1, a)), 0, 0, int(math.copysign(1, b)))
    if t1 < t2:
        (t1, t2) = (t2, t1)
        (x1, y1, x2, y2) = (x2, y2, x1, y1)
    while t2 > 0:
        if x1 * a + y1 * b != t1:
            print('inshalla')
        k = int(t1 // t2)
        (t1, t2) = (t2, t1 % t2)
        (x1, y1, x2, y2) = (x2, y2, x1 - k * x2, y1 - k * y2)
    return (t1, x1, y1)


def opposite_element(x, p):
    (gcd, k, l) = euclid_algorithm(x, p)
    if gcd != 1:
        return -1
    return k % p


def fact_mod(n, p):
    prod = 1
    for i in range(2, n + 1):
        prod *= i
        prod %= p
    return prod


k = int(input())
c = []
for i in range(k):
    c.append(int(input()))
prefix_sum = 0
p = 10 ** 9 + 7
denominator = 1
for c_i in c:
    denominator *= fact_mod(c_i - 1, p)
    denominator %= p
    prefix_sum += c_i
    denominator *= prefix_sum
    denominator %= p
numenator = fact_mod(prefix_sum, p)
print(numenator * opposite_element(denominator, p) % p)
