def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(n**.5 + 1), 2))


def S(n):
    if n == 1:
        return 4
    return S(n - 1) * S(n - 1) - 2


def mod_equiv(n, p):
    binario = bin(n)[2:]
    suma = n
    while len(binario) > p:
        suma = int(binario[-p:], 2) + int(binario[:-p], 2)
        binario = bin(suma)[2:]
    return suma


def lucas_lehmer(n):
    if not isPrime(n):
        return False
    s = 4
    M = 2**n - 1
    for i in range(n - 2):
        # s = (s*s-2) % M
        s = (mod_equiv(s * s - 2, n)) % M
    return s == 0 or n == 2
