def gen(n):
    if n >= 10**16: return
    for i in range(10):
        x = 10*n + i
        if x % sum(map(int, str(x))): continue
        yield x
        for y in gen(x): yield y
L = sorted(x for n in range(1, 10) for x in gen(n))

from bisect import bisect_left as bl, bisect_right as br
def rthn_between(a, b):
    return L[bl(L, a):br(L, b)]
