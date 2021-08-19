# Breadth first decreasing (BFD) algorithm for the Frobenius
# number following Beihoffer, Hendry, Nijenhuis, and Wagon
# ("Faster Algorithms For Frobenius Numbers", The Electronic
# Journal of Combinatorics, 2005).

from functools import reduce
from collections import deque


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def min_price(a):
    if 1 in a:
        return 1
    elif reduce(gcd, a) != 1:
        return -1

    n = len(a)
    a.sort()
    a1 = a[0]

    q = deque([0])
    h = set([0])

    p = [n] + [0] * a1
    s = [0] + [a1 * a[-1]] * (a1 - 1)
    amod = [x % a1 for x in a]

    while q:
        v = q.popleft()
        h.remove(v)

        for j in range(1, p[v]):
            u = v + amod[j]
            if u >= a1:
                u -= a1

            w = s[v] + a[j]

            # This performance-enhancing
            # condition is given on p. 10.
            if w == s[u] and j < p[u] - 1:
                p[u] = j + 1

            if w < s[u]:
                s[u] = w
                p[u] = j + 1
                if u not in h:
                    q.append(u)
                    h.add(u)

    return max(s) - a1 + 1
