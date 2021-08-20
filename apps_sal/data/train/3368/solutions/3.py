from collections import deque


def is_prime(n):
    return n > 1 and all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))


def circular_prime(n):
    items = deque(str(n))
    for _ in range(len(items)):
        items.rotate(1)
        if not is_prime(int(''.join(items))):
            return False
    return True
