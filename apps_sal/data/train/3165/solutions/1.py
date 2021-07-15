from functools import lru_cache

msb = lru_cache(maxsize=None)(lambda n: 1 << n.bit_length() - 1)

# Taken from https://oeis.org/A139250
# With some upgrades cause why not?
@lru_cache(maxsize=None)
def toothpick(n):
    if n == 0: return 0
    x = msb(n)
    res = ((x**2 << 1) + 1) // 3
    if n != x:
        res += (toothpick(n - x) << 1) + toothpick(n - x + 1) - 1
    return res
