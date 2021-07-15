from functools import lru_cache
from itertools import takewhile, count
even_fib = lru_cache(maxsize=None)(lambda n: 2 if n==0 else 8 if n==1 else 4*even_fib(n-1) + even_fib(n-2))

def SumEvenFibonacci(limit):
    return sum(takewhile(limit.__ge__, map(even_fib, count())))
