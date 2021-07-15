def is_prime_happy(n):
    primes = [2] + [x for x in range(3, n, 2) if all(x % r for r in range(3, int(x**0.5)+1, 2))]
    return n > 2 and sum(primes) % n == 0
