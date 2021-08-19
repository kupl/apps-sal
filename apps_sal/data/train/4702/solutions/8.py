from math import gcd, log
from operator import mul
from functools import reduce


def digits_product(product):
    if product <= 1:
        return 10 + product

    def count(p):
        return round(log(gcd(product, p ** 9), p))
    (n2, n3, n5, n7) = map(count, [2, 3, 5, 7])
    digits = [5] * n5 + [7] * n7 + [8] * (n2 // 3) + [9] * (n3 // 2)
    n2 %= 3
    n3 %= 2
    if n3 and n2:
        digits.append(6)
        n3 -= 1
        n2 -= 1
    digits.extend([4] * (n2 // 2) + [2] * (n2 % 2) + [3] * n3)
    if len(digits) <= 1:
        digits.append(1)
    return int(''.join(map(str, sorted(digits)))) if reduce(mul, digits) == product else -1
