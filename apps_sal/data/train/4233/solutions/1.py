def is_prime(n): return n > 1 and all(n % j for j in range(2, int(n**0.5) + 1))
def goldbach(n): return [[i, n - i] for i in range(2, int(n / 2) + 1) if is_prime(i) and is_prime(n - i)]
