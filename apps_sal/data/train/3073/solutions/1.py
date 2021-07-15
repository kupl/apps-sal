from functools import lru_cache


@lru_cache(maxsize=None)
def f(ndigits, starting_digit):
    if ndigits == 0:
        return 1
    return sum(f(ndigits-1, i) for i in range(starting_digit, 10))
    
def increasing_numbers(digits):
    if digits == 0:
        return 1
    return sum(f(digits-1, i) for i in range(10))
