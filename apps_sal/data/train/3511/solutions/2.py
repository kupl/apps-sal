def prime_factors(n):
    s, a = [], 2
    while a * a <= n:
        while n % a == 0:
            s.append(a)
            n //= a
        if a >= n:
            return s
        a += 1
    if n > 1:
        s.append(n)
    return s


def find_key(encryption_key):
    a, b = prime_factors(int(encryption_key, 16))
    return (a - 1) * (b - 1)
