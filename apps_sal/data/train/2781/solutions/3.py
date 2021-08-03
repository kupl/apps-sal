from functools import lru_cache


@lru_cache(maxsize=None)
def collatz(n):
    return n != 1 and 1 + collatz(3 * n + 1 if n & 1 else n >> 1)


def longest_collatz(input_array):
    return max(input_array, key=collatz)
