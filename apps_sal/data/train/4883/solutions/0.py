from itertools import count


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            return False
    return True


def next_prime(n):
    for candidate in count(n + 1):
        if is_prime(candidate):
            return candidate
