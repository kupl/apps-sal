import functools


@functools.lru_cache(None)
def is_prime(n):
    if n < 4:
        return True

    for i in range(3, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True


def gap(g, m, n):
    start = 0

    if m % 2 == 0:
        m += 1

    for num in range(m, n + 1, 2):
        if is_prime(num):
            if start and num - start == g:
                return [start, num]

            start = num
