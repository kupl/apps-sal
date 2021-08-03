def is_prime(n): return n == 2 or n % 2 and all(n % d for d in range(3, int(n ** .5) + 1, 2))
def order(n, k): return n and n // k + order(n // k, k)
def decomp(n): return ' * '.join(str(p) if n < 2 * p else '%d^%d' % (p, order(n, p)) for p in range(2, n + 1) if is_prime(p))
