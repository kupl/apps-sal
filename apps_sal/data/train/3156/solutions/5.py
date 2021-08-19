from math import ceil


def digits(n):
    while n >= 10:
        if n % 10 % 2 > 0:
            return False
        n //= 10
    return n % 2 == 0


def even_digit_squares(a, b):
    p = ceil(a ** 0.5)
    q = int(b ** 0.5)
    return [i * i for i in range(p, q + 1) if digits(i * i)]
