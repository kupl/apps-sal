from functools import lru_cache

@lru_cache(maxsize=None)
def make_sequences(n):
    if n<2: return n
    n&=~1
    return make_sequences(n>>1)+make_sequences(n-1)
