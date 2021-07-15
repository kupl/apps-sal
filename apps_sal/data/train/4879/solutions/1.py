from math import factorial as fact
from functools import reduce
from collections import Counter

def count_perms(matrix):
    m = [elt for line in matrix for elt in line]
    return fact(len(m)) / reduce(lambda a,b: a*b, map(fact, Counter(m).values()), 1)
