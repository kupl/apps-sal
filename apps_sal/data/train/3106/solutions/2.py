from functools import lru_cache


@lru_cache(maxsize=None)
def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


@lru_cache(maxsize=None)
def comb(n, k):
    return fact(n) // fact(k) // fact(n - k)

# https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind


def combs_non_empty_boxes(n, k):
    if n == k:
        return 1
    if n < k:
        return "It cannot be possible!"
    return sum((1, -1)[i & 1] * comb(k, i) * (k - i)**n for i in range(k + 1)) // fact(k)
