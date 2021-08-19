import numpy as np


def product(l):
    if not l:
        return None
    if 0 in l:
        return 0
#     l=sorted(l)
#     if len(l)<20:
#         print(l)
#     if len(l)>20:
#         print(len(l))
    if len(l) == 1:
        return l[0]
    p = 1
    for i in l:
        p *= i
    return p
