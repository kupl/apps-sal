from itertools import permutations
from math import factorial

def permutation_average(n):
    return round(sum(int(''.join(x)) for x in permutations(str(n))) / float(factorial(len(str(n)))))
