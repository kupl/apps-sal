from functools import reduce
def find_missing(arr1, arr2):
    from itertools import chain
    from functools import reduce
    from operator import xor
    return reduce(xor, chain(arr1, arr2))

