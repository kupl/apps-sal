from functools import reduce
from operator import add

def max_tri_sum(numbers):
    numbers = list(dict.fromkeys(numbers))
    sort_num = sorted(numbers)
    return reduce(add, sort_num[-3:])
