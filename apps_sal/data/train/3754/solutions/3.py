def prime_product(n):
    result = 0

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            result = i * (n - i)
    return result
