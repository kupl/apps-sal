def factorial(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


def is_prime(n):
    count = 2

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            count += 1
    return count == 2


def am_i_wilson(n):
    if n <= 1 or n > 563:
        return False

    return is_prime(n) and (factorial(n - 1) + 1) % (n * n) == 0
