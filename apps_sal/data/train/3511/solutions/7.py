def find_key(encryption_key):

    def is_prime(p):
        return all((p % i for i in range(3, int(p ** 0.5) + 1, 2))) and (p == 2 or p % 2)
    n = int(encryption_key, 16)
    if n % 2 == 0 and is_prime(n // 2):
        return n // 2 - 1
    for i in range(3, n + 1, 2):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return (i - 1) * (n // i - 1)
