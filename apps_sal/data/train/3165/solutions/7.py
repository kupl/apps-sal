from math import log
from functools import lru_cache

@lru_cache(5000)
def toothpick(n):
    if n == 0:
        return 0
    else:
        k = int(log(n, 2))
        i = n - 2**k
        if i == 0:
            return (2**(2*k+1)+1)/3
        else:
            return toothpick(2**k) + 2 * toothpick(i) + toothpick(i+1) - 1

# from collections import deque
# from time import monotonic
# from numpy import zeros
# from itertools import chain

# _r = zeros((5000, 5000))
# _n = 0
# _q1 = [(2500, 2500)]
# _q2 = []
# _c = 0
# _t = monotonic()

# def toothpick(n):
#     print(n)
#     nonlocal _n, _q1, _q2, _c, _t
#     t = _t
#     if n > 2100:
#         raise Exception(n)
#     r = _r
#     q1 = _q1
#     q2 = _q2
#     count = _c
#     t1 = 0
#     t2 = 0
#     for round in range(_n, n):
#         dx = 1 if round % 2 == 1 else 0
#         dy = 0 if round % 2 == 1 else 1
#         tmp = monotonic()
#         re = []
#         ap = re.append
#         r_m = 0
        
#         for xy in chain(q1, q2):

#             r_m = r[xy]
#             if r_m == 0:
#                 r[xy] = round
#                 ap(xy)
# #                 count += 1
#             else:
#                 if r_m == round:
#                     r[xy] = -1
# #                     count -= 1
#         t1 += monotonic() - tmp
#         tmp = monotonic()
#         q1 = [(xy[0]+dx, xy[1]+dy) for xy in re if r[xy] == round]
#         q2 = [(xy[0]-dx, xy[1]-dy) for xy in re if r[xy] == round]
#         count += len(q1)
#         t2 += monotonic() - tmp
    
    
#     print(n, count, monotonic() - t, t1, t2)
#     _n = n
#     _q1 = q1
#     _q2 = q2
#     _c = count
#     return count

