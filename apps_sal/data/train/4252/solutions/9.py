from functools import reduce
from operator import or_

def merge_arrays(*args): 
    return sorted(reduce(or_, map(set, args)))
