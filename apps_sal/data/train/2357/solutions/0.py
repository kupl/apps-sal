from functools import reduce


def modpow(a, n, m):
    if n == 0:
        return 1
    tmp = modpow(a, n // 2, m)
    if n % 2 == 0:
        return tmp * tmp % m
    else:
        return tmp * tmp * a % m


def modinv(a, m):
    return modpow(a, m - 2, m)


(n, m) = [int(_) for _ in input().split(' ')]
s = sum([int(_) for _ in input().split(' ')])
M = 1000000007


def product(x1, x2):
    return x1 * x2 % M


print(reduce(product, list(range(m - s + 1, m + n + 1))) * modinv(reduce(product, list(range(1, s + n + 1))), M) % M)
