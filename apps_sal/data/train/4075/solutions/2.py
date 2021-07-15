from functools import lru_cache

@lru_cache()
def f(n):
    return (1, 1, 2, 2, 3, 3)[n] if n < 6 else (f(n-1) * f(n-2) * f(n-3)) - (f(n-4) * f(n-5) * f(n-6))
    
def something_acci(num_digits):
    n, l = 8, 4
    while l < num_digits:
        n += 1
        l = len(str(f(n)))
    return n + 1, l
