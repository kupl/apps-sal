def gap(g, m, n):
    a, b = 2, 2
    for x in range(m, n + 1):
        if is_prime(x):
            a, b = b, x
            if b - a == g:
                return [a, b]
    return None


def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True
