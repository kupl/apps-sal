
from numpy import unique

def merge_arrays(first, second): 
    return sorted(unique(first + second))
