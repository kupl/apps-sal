from functools import lru_cache


@lru_cache(maxsize=1024)
def hofstadter_Q(n):
    if n in (1, 2):
        return 1
    return hofstadter_Q(n - hofstadter_Q(n - 1)) + hofstadter_Q(n - hofstadter_Q(n - 2))


# Precompute to cache values and avoid exceeding too deep recursion
for i in range(100, 1000, 100):
    hofstadter_Q(i)
