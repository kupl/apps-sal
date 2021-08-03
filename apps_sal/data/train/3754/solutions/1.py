def prime_product(n):
    def is_prime(n): return n == 2 or n > 2 and n % 2 and all(n % d for d in range(3, int(n ** .5) + 1, 2))
    for i in range(n // 2, 1, -1):
        if is_prime(i) and is_prime(n - i):
            return i * (n - i)
    return 0
