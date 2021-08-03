def goldbach_partitions(n):
    def is_prime(n): return all(n % j for j in range(2, int(n**0.5) + 1)) and n > 1
    return [] if n % 2 else [f'{i}+{n-i}' for i in range(2, int(n / 2) + 1) if is_prime(i) and is_prime(n - i)]
