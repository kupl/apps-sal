from collections import Counter
from math import factorial

def proc_arr(arr):
    perm, strng = factorial(len(arr)), []
    for k, v in sorted(Counter(arr).items()):
        perm //= factorial(v)
        strng.append(k * v)
    return [perm, int(''.join(strng)), int(''.join(strng[::-1]))]

