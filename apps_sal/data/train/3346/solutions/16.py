def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gap(g, m, n):
    for x in range(m, n + 1 - g):
        if is_prime(x) and is_prime(x + g) \
                and not any(map(is_prime, range(x + 1, x + g))):
            return [x, x + g]
