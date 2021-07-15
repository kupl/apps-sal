from functools import lru_cache


@lru_cache()
def three_details(n, count=0):
    even, odd = n//2, n//2 + n%2
    if n == 3:
        return 1
    elif n < 3:
        return 0
    return three_details(n-even) + three_details(n-odd)
