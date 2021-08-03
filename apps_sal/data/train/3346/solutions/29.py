from math import sqrt


def prime_gen(m, n):
    def is_prime(n): return all(n % i for i in range(2, int(sqrt(n) + 1)))
    for i in range(m, n + 1):
        if is_prime(i):
            yield i


def gap(g, m, n):
    z = prime_gen(m, n)
    ini = next(z)
    while True:
        end = next(z, 'fin')
        try:
            if end - ini == g:
                return [ini, end]
            else:
                ini = end
        except:
            return None
