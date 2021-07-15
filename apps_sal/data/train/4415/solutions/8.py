from math import factorial

import re

def proc_arr(arr):
    s = ''.join(sorted(arr))
    r = ''.join(reversed(s))
    low, high = int(s), int(r)
    digits = len(s)
    denominator = mul([factorial(end - start) for start, end in 
                       [m.span() for m in re.finditer('(?P<D>\d)(?P=D)*', s)]])
    return [(factorial(digits) // denominator), low, high]
    
def mul(coll):
    return 1 if not coll else coll[0] * mul(coll[1:])

