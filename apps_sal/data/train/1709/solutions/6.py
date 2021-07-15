from itertools import chain
from collections import defaultdict

def sum_for_list(lst):
    sums = defaultdict(int)
    for n in lst:
        m = n
        for p in chain([2], xrange(3, abs(n)+1, 2)):
            if m % p == 0:
                sums[p] += n
            while m % p == 0:
                m //= p
    return map(list, sorted(sums.items()))
