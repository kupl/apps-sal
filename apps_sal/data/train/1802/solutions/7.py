# BFDU algorithm from:
# Faster Algorithms for Frobenius Numbers
# the electronic journal of combinatorics 12(2005), #R27

# TODO: Implement DQQD(U) from the same paper

import heapq
import collections
from math import gcd


def frobenius(a):

    n = len(a)
    if n == 2:
        return a[0] * a[1] - a[0] - a[1]

    a.sort()
    a1, an = a[0], a[-1]
    s = [an] * a1
    s[0] = 0
    p = [0] * a1
    p[0] = n - 1
    q = [[] for _ in range(a1)]
    q[0].append(0)
    z = [0]
    amod = [-99] + [x % a1 for x in a]
    aquot = [-99] + [x // a1 for x in a]
    a = [-99] + a

    q = collections.deque([0])
    qs = {0}
    p = [0] * a1
    p[0] = n
    s = [a1 * an] * a1
    s[0] = 0

    while q:
        v = q.popleft()
        qs.remove(v)
        for j in range(2, p[v] + 1):
            u = v + amod[j]
            if u >= a1:
                u = u - a1
            w = s[v] + a[j]
            if w < s[u]:
                s[u] = w
                p[u] = j
                if u not in qs:
                    q.append(u)
                    qs.add(u)
            elif w == s[u] and j < p[u]:
                p[u] = j
    return max(s) - a1


def min_price(a):

    if 1 in a:
        return 1
    if not a:
        return -1

    cd = a[0]
    for z in a:
        cd = gcd(cd, z)
    if cd != 1:
        return -1

    return frobenius(a) + 1
