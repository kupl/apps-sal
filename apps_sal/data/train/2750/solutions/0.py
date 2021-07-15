from functools import lru_cache

@lru_cache(maxsize=None)
def make_sequences(n):
    return 1 + sum(map(make_sequences, range(1, n//2+1)))
