
from functools import lru_cache


def survivor(zombies):
    if not zombies:
        return -1
    nums = sorted(zombies)
    represent = lru_cache(maxsize=None)(lambda x: not x or any(represent(x - y) for y in nums[::-1] if x >= y))
    maxi = nums[-1]
    current = [0] * maxi
    for x in range(0, maxi**2, maxi):
        temp = [current[i] or represent(x + i) for i in range(maxi)]
        if temp == current:
            return -1
        if all(temp):
            y = next(i for i, v in enumerate(current[::-1]) if not v)
            return max(0, x - y - 1)
        current = temp
