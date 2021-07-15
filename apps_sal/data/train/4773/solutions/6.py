from bisect import insort
from functools import reduce

def count_find_num(primesL, n):
    product = reduce(lambda a, b: a * b, primesL)
    if product > n:
        return []
    p = [product]
    last = None
    count = 0
    while p:
        first = p.pop(0)
        if first == last:
            continue
        count += 1
        for x in primesL:
            m = x * first
            if m <= n:
                insort(p, m)
        last = first
    return [count, last] if count else []
