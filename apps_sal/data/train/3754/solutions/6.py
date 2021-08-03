def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def prime_product(n):
    for i in range(n // 2 + 1)[::-1]:
        if is_prime(i) and is_prime(n - i):
            return i * (n - i)
    return 0
