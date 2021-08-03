from math import log10
from decimal import Decimal


def solve(n, k):

    mod = 10**k
    x = Decimal(n)
    y = x * (x.log10()) % 1
    p = str(pow(10, y))
    c = 0
    first = ''
    for v in p:
        if c == k:
            break
        if v == ".":
            continue
        first += v
        c += 1
    last = str(pow(n, n, mod)).zfill(k)
    return (first, last)


queries = []
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    queries.append((n, k))
for n, k in queries:
    print("%s %s" % (solve(n, k)))
