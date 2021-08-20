from functools import lru_cache
visited = set()


@lru_cache(maxsize=None)
def happy(n):
    if n == 1 or n in visited:
        visited.clear()
        return n == 1
    visited.add(n)
    n = sum((int(digit) ** 2 for digit in str(n)))
    return happy(n)


def happy_numbers(n):
    return [i for i in range(1, n + 1) if happy(i)]
