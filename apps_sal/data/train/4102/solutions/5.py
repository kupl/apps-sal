def odd_not_prime(n):
    return len([x for x in range(1, n + 1, 2) if not (not any([x % y == 0 for y in range(3, int(x ** (1 / 2)) + 1, 2)]) and x != 1)])
