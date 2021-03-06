from itertools import count
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def convert_digits(s):
    return [int(digits.index(d)) for d in s]


def convert_to_base_10(s, b):
    if b == 10:
        return s
    coeffs = convert_digits(s)[::-1]
    return str(sum([coeffs[i] * b ** i for i in range(len(s))]))


def convert_from_base_10(s, b):
    max_exp = 0
    n = int(s)
    coeffs = []
    while b ** (max_exp + 1) <= n:
        max_exp += 1
    for k in range(max_exp + 1):
        coeffs.append(digits[n % b])
        n = int((n - n % b) / b)
    return ''.join(coeffs[::-1])


def is_polydivisible(s, b):
    base_b = [s[:k] for k in range(1, len(s) + 1)]
    base10 = list(map(lambda s: convert_to_base_10(s, b), base_b))
    divisible = [int(base10[k]) % (k + 1) == 0 for k in range(1, len(s))]
    return not False in divisible


def get_polydivisible(n, b):
    poly_count = 0
    for k in count(start=0, step=1):
        if is_polydivisible(convert_from_base_10(str(k), b), b):
            temp = str(k)
            poly_count += 1
            if poly_count == n:
                return convert_from_base_10(temp, b)
