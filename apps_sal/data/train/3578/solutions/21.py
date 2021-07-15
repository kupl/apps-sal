from operator import mul
from functools import reduce

def paperwork(*args):
    return reduce(mul, args) if min(args) > 0 else 0
