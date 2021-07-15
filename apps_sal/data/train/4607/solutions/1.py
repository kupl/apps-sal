from collections import Counter
from functools import reduce
from itertools import combinations
from math import factorial
from operator import mul

def find_mult_3(n):
    mul_count, digits = 0, sorted(map(int, str(n)))
    for r in range(1, len(digits) + 1):
        for comb in sorted({c for c in combinations(digits, r) if not sum(c) % 3}):
            dig_count = Counter(comb)
            mul_count += (r - dig_count.get(0, 0)) * factorial(r) // reduce(mul, map(factorial, dig_count.values()), r)
    return [mul_count, int(''.join(map(str, comb[::-1])))]
