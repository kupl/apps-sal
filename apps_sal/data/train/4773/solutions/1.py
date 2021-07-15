from functools import reduce

def count_find_num(primesL, limit):
    def rec(n, primes):
        if not primes: return
        x, (y, *next_primes) = n, primes
        while x <= limit:
            if x != n: yield x
            yield from rec(x, next_primes)
            x *= y
    
    start = reduce(int.__mul__, primesL)
    if start > limit: return []
    result = [start] + list(rec(start, primesL))
    return [len(result), max(result)]
