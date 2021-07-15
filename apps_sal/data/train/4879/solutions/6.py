from math import factorial
from collections import Counter
from functools import reduce

def count_perms(matrix):
    items = [a for b in matrix for a in b]
    return factorial(len(items)) // reduce(lambda x,y: x*y, list(map(factorial, list(Counter(items).values()))), 1)

