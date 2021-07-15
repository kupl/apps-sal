from math import factorial
from collections import Counter
from functools import reduce

def uniq_count(s):
    return factorial(len(s)) // reduce(lambda x, y: x * factorial(y) , Counter(s.lower()).values(), 1)
